#include <iostream>
#include "foo-0.h"
#include "foo-1.h"

int main( int count, char * * args )
{
	std::cout << Foo0() << "\n" << Foo1();
}
