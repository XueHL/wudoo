#include <iostream>

#include "NameHolder.h"

int main( int count, char * * args )
{
	std::cout << "User-0\n";
	NameHolder nameHolder;
	std::cout << nameHolder.GetName();
	return 0;
}
