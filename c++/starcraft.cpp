#include <iostream>
#include <string.h>

class Marine {
  int hp;                // 마린 체력
  int coord_x, coord_y;  // 마린 위치
  int damage;            // 공격력
  bool is_dead;
  char* name; // 마린 이름

 public:
  Marine();              // 기본 생성자
  Marine(int x, int y, const char* marine_name);  // 이름까지 지정
  Marine(int x, int y);  // x, y 좌표에 마린 생성
  ~Marine(); // 소멸자

  int attack();                       // 데미지를 리턴한다.
  void be_attacked(int damage_earn);  // 입는 데미지
  void move(int x, int y);            // 새로운 위치

  void show_status();  // 상태를 보여준다.
};
Marine::Marine() {
  hp = 50;
  coord_x = coord_y = 0;
  damage = 5;
  is_dead = false;
  name = NULL;
}
Marine::Marine(int x, int y, const char* marine_name) {
  name = new char[strlen(marine_name) + 1];
  strcpy(name, marine_name);

  coord_x = x;
  coord_y = y;
  hp = 50;
  damage = 5;
  is_dead = false;
}
Marine::Marine(int x, int y) {
  coord_x = x;
  coord_y = y;
  hp = 50;
  damage = 5;
  is_dead = false;
  name = NULL;
}
void Marine::move(int x, int y) {
  coord_x = x;
  coord_y = y;
}
int Marine::attack() { return damage; }
void Marine::be_attacked(int damage_earn) {
  hp -= damage_earn;
  if (hp <= 0) is_dead = true;
}
void Marine::show_status() {
  std::cout << " *** Marine : " << name << " ***" << std::endl;
  std::cout << " Location : ( " << coord_x << " , " << coord_y << " ) "
            << std::endl;
  std::cout << " HP : " << hp << std::endl;
}
Marine::~Marine() {
  std::cout << name << " 의 소멸자 호출 ! " << std::endl;
  if (name != NULL) {
    delete[] name;// name이 char의 배열로 동적할당 하였기때문에 []써야함
  }
}

int main() {
  Marine* marines[100];
  // 생성자 new
  marines[0] = new Marine(2, 3, "Marine 2");
  marines[1] = new Marine(1, 5, "Marine 1");
//   Marine marine1(2, 3);
//   Marine marine2(3, 5);
/* 포인터를 가리키는 배열이기 때문에
   메소드를 호출할때 .가 아닌 ->를 사용*/ 
  marines[0]->show_status();
  marines[1]->show_status();
//   marine1.show_status();
//   marine2.show_status();
  std::cout << std::endl << "마린 1 이 마린 2 를 공격! " << std::endl;
//   marine2.be_attacked(marine1.attack());
  marines[0]->be_attacked(marines[1]->attack());
  
  marines[0]->show_status();
  marines[1]->show_status();
//   marine1.show_status();
//   marine2.show_status();
  delete marines[0]; // new(동적으로할당한 메모리)는 언제나 해제
  delete marines[1];
}