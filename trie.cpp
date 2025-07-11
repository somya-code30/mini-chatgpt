# Placeholder for trie.cpp
#include "trie.h"

TrieNode::TrieNode() {
    isEndOfWord = false;
    for (int i = 0; i < 26; i++)
        children[i] = nullptr;
}

Trie::Trie() {
    root = new TrieNode();
}

void Trie::insert(const std::string& word, const std::string& response) {
    TrieNode* node = root;
    for (char ch : word) {
        int index = tolower(ch) - 'a';
        if (index < 0 || index >= 26) continue; // Ignore non-alphabetic
        if (!node->children[index])
            node->children[index] = new TrieNode();
        node = node->children[index];
    }
    node->isEndOfWord = true;
    node->response = response;
}

std::string Trie::search(const std::string& word) {
    TrieNode* node = root;
    for (char ch : word) {
        int index = tolower(ch) - 'a';
        if (index < 0 || index >= 26 || !node->children[index])
            return "";
        node = node->children[index];
    }
    return node->isEndOfWord ? node->response : "";
}
