#include<iostream.h>

#include"SufString.h"

SufString::SufString( char * text )
{
	this->text = text;
	std::cout << "created\n";
}

SufString::~SufString()
{
	this->text = text;
	std::cout << "destroyed\n";
}

char * SufString::Get()
{
	return text;
}
