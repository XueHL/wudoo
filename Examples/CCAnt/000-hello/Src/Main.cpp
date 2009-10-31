#include <iostream>
#include "Hello.h"

int main( int count, char * * args )
{
	Hello hello( count );
	std::cout << hello.Get();
}
