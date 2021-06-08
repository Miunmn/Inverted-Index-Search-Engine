#include<iostream>
#include "inverted_index.h"
using namespace std;

int main(int argc, char*argv[])
{
  InvertedIndex Data;
  for(int i = 1 ; i< argc ; i++)
  {
    Data.addfile(argv[i]);
  }

  Data.addfile("datos.txt");


  return 0;
}
