#include <iostream>
#include "jniant_CPPHello.h"

JNIEXPORT void JNICALL Java_jniant_CPPHello_printHello
  (JNIEnv * env, jobject obj)
{
	std::cout << "Hello!\n";
}
