#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#	   Package Comments 0.1
#	   Copyright 2011 Mladen Mijatov <meaneye.rcf@gmail.com>
#
#	   This program is free software; you can redistribute it and/or modify
#	   it under the terms of the GNU General Public License as published by
#	   the Free Software Foundation; either version 2 of the License, or
#	   (at your option) any later version.
#	   
#	   This program is distributed in the hope that it will be useful,
#	   but WITHOUT ANY WARRANTY; without even the implied warranty of
#	   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	   GNU General Public License for more details.
#	   
#	   You should have received a copy of the GNU General Public License
#	   along with this program; if not, write to the Free Software
#	   Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#	   MA 02110-1301, USA.
#	   
#	   
"""
	This script is used to get comments and ratings for specified package
	from Ubuntu software center. Please note that not all packages have comments!
"""

import os
import sys
import json
import time
import urllib2
import textwrap

from threading import Thread
from argparse import ArgumentParser


class PackageComments:

	NAME = 'Package Comments'
	VERSION = '0.2'
	LOCALE = 'en'
	BASE_URL = 'http://reviews.ubuntu.com/reviews/api/1.0/reviews/filter/{0}/ubuntu/{1}/any/{2}/page/{3}'
	TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

	def __init__(self):
		self.arguments = None
		self.output_file = None
		self.terminal_size = (25, 80)
		self.padding = 11
		
		self.__line_counter = 0

	def __parse_arguments(self):
		"""Parse command line arguments and configure application accordingly"""
		
		parser = ArgumentParser(description=self.NAME)

		# add arguments
		parser.add_argument('package', help='Package name to get comments for.')
		parser.add_argument('-v', action='version', version=self.VERSION, help='Print script version and exit.')
		parser.add_argument('-q', action='store_true', dest='quiet', help='Operate in quiet mode. Print only data.')
		parser.add_argument('-r', dest='release', default='oneiric', help='Specify Ubuntu release name [natty, oneiric, ..].')
		parser.add_argument('-o', dest='output_file', help='Save output to a file.')
		parser.add_argument('-s', action='store_true', dest='simple', help='Make output simple.')
		parser.add_argument('-t', action='store_true', dest='show_timestamp', help='Show timestamp in output.')
		parser.add_argument('-g', action='store_true', dest='show_version', help='Show package version in output.')
		parser.add_argument('-k', action='store', dest='column', default='id', help='Sort items by column [rating, age, id, user].')
		parser.add_argument('-d', action='store_true', dest='sort_descending', help='Sort data in descending order.')
		parser.add_argument('-p', action='store_true', dest='pause_display', help='Display one screen at a time. Pause after reaching end of the screen.')

		# parse arguments
		self.arguments = parser.parse_args()
		
	def __compare_function(self, item1, item2):
		"""Compare two items"""
		result = 0
		
		if self.arguments.column == 'rating':
			# compare by rating
			result = cmp(item1['rating'], item2['rating'])
			
		elif self.arguments.column == 'age':
			# compare by time stamp
			time1 = time.strptime(item1['date_created'], self.TIME_FORMAT)
			time2 = time.strptime(item2['date_created'], self.TIME_FORMAT)
			
			result = cmp(time1, time2)
			
		elif self.arguments.column == 'user':
			# compare by user name
			result = cmp(item1['reviewer_username'], item2['reviewer_username'])
			
		else:
			result = cmp(item1['id'], item2['id'])
		
		return result

	def __get_review_page(self, page=1):
		"""Get user reviews on specified page"""
		url = self.BASE_URL.format(
							self.LOCALE,
							self.arguments.release,
							self.arguments.package,
							page
						)
		
		# get reviews for specified page
		socket = urllib2.urlopen(url)
		data = socket.read()
		socket.close()

		# parse results
		result = json.loads(data)
		
		return result

	def __get_reviews(self, page=1):
		"""Get reviews, parse them and return dictionary list"""
		result = []
		
		if not self.arguments.quiet: 
			print 'Downloading user reviews:'

		# get first page of reviews
		current_page = 1
		reviews = self.__get_review_page(current_page)

		if len(reviews) > 0:
			# package exists and there are some comments
			# try to load others
			
			while len(reviews) > 0:
				# add reviews to the result list
				result.extend(reviews)
				
				# notify user
				if not self.arguments.quiet:
					print "   page {0}: {1}".format(current_page, len(reviews))
					
				# try to get next page
				current_page += 1
				reviews = self.__get_review_page(current_page)
				
		# sort items
		result.sort(self.__compare_function, reverse=self.arguments.sort_descending)

		return result
		
	def __print_line(self, text):
		"""Printe preformated text to file or screen"""
		if self.output_file is None:
			# pause if needed
			if self.arguments.pause_display:
				self.__line_counter += text.count('\n') + 1
				
				# pause if we are printing on the last line in the screen
				if self.__line_counter >= self.terminal_size[0]:
					self.__line_counter = 0
					raw_input('Press return to continue...')

			#  print text on screen
			print text
			
		else:
			# write text to opened text file
			self.output_file.write(text + '\n')
		
	def __print_review(self, review):
		"""Print review to screen or save it to file"""
		
		# fix unicode characters
		for key, value in review.iteritems():
			review[key] = unicode(value).encode('utf-8')

		# format user name
		if review.has_key('reviewer_displayname'):
			user = '{0} ({1})'.format(review['reviewer_displayname'], review['reviewer_username'])
			
		else:
			user = review['reviewer_username']
		
		# print header
		if not self.arguments.simple:
			# print header with all details
			text = '{0}{1} id: {2} rating: {3} origin: {4}'.format(
												'user:'.ljust(self.padding),
												user.ljust(40),
												review['id'].ljust(10),
												review['rating'].ljust(3),
												review['origin'],
											)
											
			self.__print_line(text)
			
		else:
			# print short header
			self.__print_line('{0}{1} / {2}'.format('user:'.ljust(self.padding), user, review['rating']))
			
		# print time stamp
		if self.arguments.show_timestamp:
			self.__print_line('{0}{1}'.format('timestamp:'.ljust(self.padding), review['date_created']))
			
		# print package version
		if self.arguments.show_version:
			self.__print_line('{0}{1}'.format('version:'.ljust(self.padding), review['version']))
			
		# print summary
		if not self.arguments.simple:
			self.__print_line('{0}{1}'.format('summary:'.ljust(self.padding), review['summary']))
		
		# print review text
		text = textwrap.wrap(review['review_text'], self.terminal_size[1] - self.padding)
		text = '\n'.join(map(lambda line: ' ' * self.padding + line, text)).lstrip()
		self.__print_line('{0}{1}\n'.format('review:'.ljust(self.padding), text))
		
	def __get_terminal_size(self):
		"""Get terminal window size"""
		return os.popen('stty size', 'r').read().split()
			
	def run(self):
		"""Parse arguments and run application"""
		self.__parse_arguments()
		
		# get terminal size
		self.terminal_size = map(lambda x: int(x), self.__get_terminal_size())

		# print basic information
		if not self.arguments.quiet:
			print '{0} {1}'.format(self.NAME, self.VERSION)
			print 'Copyright (c) 2011. by MeanEYE.rcf\n'
			print 'Release: {0}'.format(self.arguments.release)
			print 'Package: {0}\n'.format(self.arguments.package)

		# get reviews
		reviews = self.__get_reviews()

		if not self.arguments.quiet:
			print 'Got total of {0} user reviews!'.format(len(reviews))

		# open file if needed
		if self.arguments.output_file is not None:
			try:
				self.output_file = open(self.arguments.output_file, 'w+')
			
			except:
				print 'Error opening specified file: {0}'.format(self.arguments.output_file)
				sys.exit(1)

		# show or save all reviews
		map(self.__print_review, reviews)
		
		# close file if open
		if self.output_file is not None:
			self.output_file.close()


if __name__ == '__main__':
	application = PackageComments()
	application.run()

