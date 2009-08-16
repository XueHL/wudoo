#include <iostream>
#include "ExportHello.h"

int main( int count, char * * args )
{
	ExportHello exportHello;
	std::cout << exportHello.Get();
}
