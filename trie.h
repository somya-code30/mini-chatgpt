# Placeholder for trie.h
#ifndef TRIE_H
#define TRIE_H

#include <string>

struct TrieNode {
    TrieNode* children[26];
    bool isEndOfWord;
    std::string response;

    TrieNode();
};

class Trie {
private:
    TrieNode* root;

public:
    Trie();
    void insert(const std::string& word, const std::string& response);
    std::string search(const std::string& word);
};

#endif
