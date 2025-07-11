#include "chatbot_engine.h"

ChatbotEngine::ChatbotEngine() {
    trie = new Trie();
}

void ChatbotEngine::addKeywordResponse(const std::string& keyword, const std::string& response) {
    trie->insert(keyword, response);
}

std::string ChatbotEngine::getResponse(const std::string& query) {
    std::string response = trie->search(query);
    if (response.empty()) {
        return "Sorry, I don't understand that yet.";
    }
    return response;
}
