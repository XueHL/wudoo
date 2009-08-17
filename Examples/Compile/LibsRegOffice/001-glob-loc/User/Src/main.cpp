#include <iostream>

#include "GLUser.h"

#include "Global.h"
#include "Local.h"

int main( int count, char * * args )
{
	std::cout << GET_GLOBAL_NAME_METHOD() << "\n";
	std::cout << GET_LOCAL_NAME_METHOD() << "\n";
	return 0;
}
