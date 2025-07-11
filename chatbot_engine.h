# Placeholder for chatbot_engine.h
#ifndef CHATBOT_ENGINE_H
#define CHATBOT_ENGINE_H

#include "trie.h"
#include <string>

class ChatbotEngine {
private:
    Trie* trie;

public:
    ChatbotEngine();
    void addKeywordResponse(const std::string& keyword, const std::string& response);
    std::string getResponse(const std::string& query);
};

#endif
