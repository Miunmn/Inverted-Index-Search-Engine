#include<iostream>
#include<vector>
#include<map>
#include<string>
#include<fstream>
#include<sstream>

struct word_position
{
  std::string file_name;
  int line;
  int index;
};

class InvertedIndex
{
  std::map<std::string,std::vector<word_position> > Dictionary;
  std::vector<std::string> filelist;

  public:
    void addfile(std::string filename);
    void show_files();
    void search(std::string word);
};

void InvertedIndex::addfile(std::string filename)
{
  std::ifstream fp;
  fp.open(filename,std::ios::in);

  if(!fp)
  {
    std::cout<<"File Not Found\n";
    return ;
  }

  filelist.push_back(filename);

  std::string line,word;
  int line_number=0,word_number=0;
  while(getline(fp,line))
  {
    line_number++;
    word_number = 0;
    std::stringstream s(line);
    while(s>>word)
    {
      word_number++;
      word_position obj;
      obj.file_name = filename;
      obj.line = line_number;
      obj.index = word_number;
      Dictionary[word].push_back(obj);
    }
  }
  fp.close();
}

void InvertedIndex::show_files()
{
  int size = (int)filelist.size();
  for(int i=0;i<size;i++) std::cout<<i+1<<": "<<filelist[i]<<std::endl;

  if(!size) std::cout<<"No files added\n";
}

void InvertedIndex::search(std::string word)
{
  if(Dictionary.find(word)==Dictionary.end())
  {
    std::cout<<"No instance exist\n";
    return ;
  }


  int size = (int)Dictionary[word].size();
  for(int counter = 0;counter < size ;counter++)
  {
    std::cout<<counter+1<<":\n";
    std::cout<<"   Filename: "<<Dictionary[word][counter].file_name<<std::endl;
    std::cout<<"   Line Number: "<<Dictionary[word][counter].line<<std::endl;
    std::cout<<"   Index: "<<Dictionary[word][counter].index<<std::endl;
  }
}
