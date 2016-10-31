// Framework for running and testing project euler problems.
#ifndef __pe_h
#define __pe_h

#include <iostream>

namespace pe {

  template <class T>
  bool test(T result, T expected) {
    bool r = (result == expected);
    if (r) {
      std::cout << "Test passed!" << std::endl;
    } else {
      std::cout << "Test failed. Got " << result << " expected " 
        << expected << std::endl;
    }
    return r;
  }

}

#endif
