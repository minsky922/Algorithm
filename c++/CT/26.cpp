#include <sstream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

vector<int> solution(vector<string> id_list, vector<string> report, int k) {
  vector<int> answer;
  unordered_map<string, unordered_set<string>> report_dic;
  unordered_map<string, int> report_num;

  for (string &r : report) {
    stringstream ss(r);
    string user_id, reported_id;
    ss >> user_id >> reported_id;
    report_dic[reported_id].insert(user_id);
  }
  for (auto &[reported_id, user_id_list] : report_dic) {
    if (user_id_list.size() >= k) {
      for (const string &uid : user_id_list) {
        report_num[uid]++;
      }
    }
  }
  for (string &id : id_list) {
    answer.push_back(report_num[id]);
  }
  return answer;
}