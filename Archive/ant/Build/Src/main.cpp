#include <iostream>
#include "ExportHello.h"

int main( int count, char * * args )
{
	ExportHello exportHello;
	std::cout << "I use export hel lo\n";
	std::cout << exportHello.Get();
}
