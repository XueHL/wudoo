#include <iostream>
#include "sharedptrtest.h"

int main( int count, char * * args )
{
	std::cout << "shared_ptr created: " << ShPtrTst::Created() << " shared_ptr destroyed: " << ShPtrTst::Destroyed() << "\n";
	RunShPtrTest();
	std::cout << "shared_ptr created: " << ShPtrTst::Created() << " shared_ptr destroyed: " << ShPtrTst::Destroyed() << "\n";
}
