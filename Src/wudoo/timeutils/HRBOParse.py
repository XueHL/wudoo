# -*- coding: windows-1251 -*-

import datetime

START_CALENDAR_PATTERN = "Пн. 	Вт. 	Ср. 	Чт. 	Пт. 	Сб. 	Вс."

def getMonthStart():
	nw = datetime.datetime.now()
	return datetime.date(year = nw.year, month = nw.month, day = 1)

def eatDayNumber(buf_ptr, date):
	day = date.day
	day = str(day)
	daypos = buf_ptr[0].find(day)
	assert daypos > -1
	daypos += len(day)
	buf_ptr[0] = buf_ptr[0][daypos:]

def parseSqbrbuf(buf_ptr):
	op = buf_ptr[0].find("[")
	assert op > -1
	if op > 1:
		return None
	cp = buf_ptr[0].find("]")
	assert cp > -1
	result = buf_ptr[0][op+1:cp]
	buf_ptr[0] = buf_ptr[0][cp+1:]
	return result

def isDigit(d):
	return d >= '0' and d <= '9'

def parseTime(buf_ptr, date):
	ddp = buf_ptr[0].find(":")
	qstp = buf_ptr[0].find("?")
	if qstp < ddp and qstp > -1:
		buf_ptr[0] = buf_ptr[0][qstp+1:]
		nw = datetime.datetime.now()
		return datetime.datetime(year = nw.year, month = nw.month, day = nw.day, hour = nw.hour, minute = nw.minute)
	if ddp > 3:#vihodnoy
		return None
	assert ddp > -1
	bp = ddp - 1
	assert isDigit(buf_ptr[0][bp])
	if bp > 0 and isDigit(buf_ptr[0][bp - 1]):
		bp -= 1
	ep = ddp + 3
	#resultBuf = buf_ptr[0][bp:ep]
	hour = buf_ptr[0][bp:ddp]
	hour = int(hour)
	minute = buf_ptr[0][ddp+1:ep]
	minute = int(minute)
	buf_ptr[0] = buf_ptr[0][ep:]
	return datetime.datetime(year = date.year, month = date.month, day = date.day, hour = hour, minute = minute)

def eatDayDistSep(buf_ptr):
	p = buf_ptr[0].find(" - ")
	assert p == 0
	buf_ptr[0] = buf_ptr[0][3:]

class WorkDist:
	def __init__(self, dayBegTime, dayEndTime):
		self.dayBegTime = dayBegTime
		self.dayEndTime = dayEndTime

	def __str__(self):
		return str(self.dayBegTime) + " -> " + str(self.dayEndTime) + " :: " + str(self.dayEndTime - self.dayBegTime)

class WorkDay:
	def __init__(self):
		self.__workDists = []

	def append(self, workDist):
		self.__workDists.append(workDist)

	def getTotalWorkTime(self):
		result = datetime.timedelta(days = 0)
		for workDist in self.__workDists:
			result = result + ( workDist.dayEndTime - workDist.dayBegTime )
		return result

	def __str__(self):
		buf = str(self.getTotalWorkTime()) + " ::: "
		for wirkDist in self.__workDists:
			buf = buf + str(wirkDist) + ", "
		if not self.isEmpty():
			buf = buf[:len(buf)-2]
		return buf

	def isEmpty(self):
		return len(self.__workDists) == 0


class WorkWeek:
	def __init__(self, workDays):
		self.workDays = workDays

def parseMonth(buf):
	p = buf.find(START_CALENDAR_PATTERN)
	p += len(START_CALENDAR_PATTERN)
	buf = buf[p:]
	date = getMonthStart()
	initMonth = date.month
	deltaOneDay = datetime.timedelta(days = 1)
	buf_ptr = [buf]
	weeks = []
	lastWeek = [None] * 7
	while date.month == initMonth:
		eatDayNumber(buf_ptr, date)
		qsbrbuf = parseSqbrbuf(buf_ptr)
		#
		workDay = WorkDay()
		while True:
			dayBegTime = parseTime(buf_ptr, date)
			if dayBegTime is None:
				break
			eatDayDistSep(buf_ptr)
			dayEndTime = parseTime(buf_ptr, date)
			workDist = WorkDist(dayBegTime, dayEndTime)
			workDay.append(workDist)
		lastWeek[date.weekday()] = workDay
		#
		date += deltaOneDay
		if date.weekday() == 0 and (not lastWeek == [None] * 7):
			weeks.append(WorkWeek(lastWeek))
			lastWeek = [None] * 7
	if not lastWeek[0].isEmpty():
		weeks.append(WorkWeek(lastWeek))
	return weeks
