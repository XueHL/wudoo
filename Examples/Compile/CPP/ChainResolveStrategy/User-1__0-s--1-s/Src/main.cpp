#include <iostream>

#include "NameHolder0.h"
#include "NameHolder1.h"

int main( int count, char * * args )
{
	std::cout << "User-0\n";
	NameHolder0 nameHolder0;
	std::cout << nameHolder0.GetName();
	std::cout << "\nUser-1\n";
	NameHolder1 nameHolder1;
	std::cout << nameHolder1.GetName();
	return 0;
}
