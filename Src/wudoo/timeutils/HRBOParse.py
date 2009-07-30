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

def parseTime(buf_ptr):
	ddp = buf_ptr[0].find(":")
	assert ddp > -1
	bp = ddp - 1
	assert isDigit(buf_ptr[0][bp])
	if bp > 0 and isDigit(buf_ptr[0][bp - 1]):
		bp -= 1
	ep = ddp + 3
	resultBuf = buf_ptr[0][bp:ep]
	buf_ptr[0] = buf_ptr[0][ep:]
	return resultBuf

def eatDayDistSep(buf_ptr):
	p = buf_ptr[0].find(" - ")
	assert p == 0
	buf_ptr[0] = buf_ptr[0][3:]

class WorkDay:
	def __init__(self, dayBegTime, dayEndTime):
		self.dayBegTime = dayBegTime
		self.dayEndTime = dayEndTime

	def __str__(self):
		return self.dayBegTime + " -> " + self.dayEndTime

class WorkWeek:
	def __init__(self, dayDists):
		self.dayDists = dayDists

def parseMonth(buf):
	p = buf.find(START_CALENDAR_PATTERN)
	p += len(START_CALENDAR_PATTERN)
	buf = buf[p:]
	date = getMonthStart()
	initMonth = date.month
	delta = datetime.timedelta(days = 1)
	buf_ptr = [buf]
	weeks = []
	lastWeek = [None] * 7
	while date.month == initMonth:
		eatDayNumber(buf_ptr, date)
		qsbrbuf = parseSqbrbuf(buf_ptr)
		if qsbrbuf is not None:
			dayBegTime = parseTime(buf_ptr)
			eatDayDistSep(buf_ptr)
			dayEndTime = parseTime(buf_ptr)
			lastWeek[date.weekday()] = WorkDay(dayBegTime, dayEndTime)
		date += delta
		if date.weekday() == 0:
			weeks.append(WorkWeek(lastWeek))
			lastWeek = [None] * 7
	if lastWeek[0] is not None:
		weeks.append(WorkWeek(lastWeek))
	return weeks
