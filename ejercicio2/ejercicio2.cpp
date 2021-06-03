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

  int choice = 0;
  do
  {
    cout<<"1: See files\n2: Add File\n3: Query Word\n4: Exit\n";
    cin>>choice;
    switch(choice)
    {
      case 1: Data.show_files(); break;
      case 2:
      {
        cout<<"Enter File Name: ";
        string name;
        cin>>name;
        Data.addfile(name);
        break;
      }

      case 3:
      {
        cout<<"Enter Word: ";
        string word;
        cin>>word;
        Data.search(word);
        break;
      }

      case 4: break;

      default : continue;
    }
  }while(choice!=4);

  return 0;
}
