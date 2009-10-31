#include <iostream>
#include "ExportHello.h"

int main( int count, char * * args )
{
	ExportHello exportHello;
	std::cout << "I use export hello\n";
	std::cout << exportHello.Get();
}
