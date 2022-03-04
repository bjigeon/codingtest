// // https://learnjs.vlpt.us/basics/


// // 출력 : console.log('JavaScript');
// // JavaScript

// 변수와 상수

// 변수
// let value = 1;
// console.log(value);
// value = 2;
// console.log(value);

// 상수
// const a = 1;
// a = 2;

// 안됨
// const a = 1;
// const a = 2;

// VAR
// var a = 1;
// var 이 let 과 다른 주요 차이점으로는, 똑같은 이름으로 여러번 선언 할 수도 있습니다.

//     문자열
// let text = 'hello';
// let name = '좌봐스크립트';

// 참 / 거짓
// let good = true;
// let loading = false;

// NULL
// null 은 주로, 이 값이 없다! 라고 선언을 할 때 사용합니다.

//     UNDEFINED
// 아직 값이 설정되지 않은 것을 의미
// let criminal;
// console.log(criminal);
// undefined

// 연산자
// let value = 1; // 변수 선언
// value = 2; // 대입 연산자

// 산술 연산자
//     + : 덧셈
//         - : 뺼셈
//             * : 곱셈
//                 / : 나눗셈

// let a = 1 + 2;
// console.log(a);

// let a = 1 + 2 - (3 * 4) / 4;
// console.log(a);

// let a = 1;
// a++;
// ++a;
// console.log(a);

// let a = 1;
// console.log(a++);
// console.log(++a);

// 대입 연산자
// let a = 1;
// console.log(a++);
// console.log(++a);

// let a = 1;
// a += 3;

// let a = 1;
// a += 3;
// a -= 3;
// a *= 3;
// a /= 3;
// console.log(a);

// 논리 연산자
// ! : NOT
//     && : AND
//         || : OR

// NOT
// const a = !true;
// console.log(a); false
// const b = !false
// console.log(a); true

// AND
// 양쪽의 값이 둘 다 true 일때만 결과물이 true

// const a = true && true;
// console.log(a);

// OR
// 양쪽의 값 중 하나라도 true 라면 결과물이 true
// 두 값이 둘 다 false 일 때에만 false
// let t = true || false;
// t = false || true;
// t = true || true;
// let f = false || false;

// 연산 순서
// NOT -> AND -> OR
// const value = !((true && false) || (true && false) || !false);
// 1.NOT
// !((true && false) || (true && false) || true);
// 2.AND
// !(false || false || true);
// 3.OR
// !true;

// 비교 연산자
//     === 는 두 값이 일치하는지 확인해줍니다.일치한다면, true, 일치하지 않는다면 false
// const a = 1;
// const b = 1;
// const equals = a === b;
// console.log(equals);

// = 문자가 3개 있을 때와 2개 있을 떄의 차이점은 2개 있을때에는 타입 검사까지는 하지 않는다
// const a = 1;
// const b = 1;
// const equals = a == b;
// console.log(equals);

// const a = 1;
// const b = '1';
// const equals = a == b;
// console.log(equals);
// true

// const a = 0;
// const b = false;
// const equals = a == b;
// console.log(equals);
// true

// const a = null;
// const b = undefined;
// const equals = a == b;
// console.log(equals);
// true

// 두 값이 일치하는 않하는 확인
// 두 값이 일치하지 않는지 확인 할 때에는 !== 를 사용
// const value = 'a' !== 'b';
// true

//     != 를 사용하게 되면 타입 검사를 하지 않습니다.
//         console.log(1 != '1'); //false
// console.log(1 !== '1'); //true

// 크고 작음
// const a = 10;
// const b = 15;
// const c = 15;

// console.log(a < b); // true
// console.log(b > a); // true
// console.log(b >= c); // true
// console.log(a <= c); // true
// console.log(b < c); // false;

// 문자열 붙이기
// const a = '안녕';
// const b = '하세요';
// console.log(a + b); // 안녕하세요

// 조건문
// IF 문
// const a = 1;
// if (a + 1 === 2) {
//     console.log('a + 1 이 2 입니다.');
// }

// const a = 1;
// if (true) {
//     const a = 2;
//     console.log('if문 안의 a 값은 ' + a);
// }
// console.log('if문 밖의 a 값은 ' + a);
// "if문의 안의 a 값은 2"
// "if문 밖의 a 값은 1"

// IF ELSE 문
// const a = 10;
// if (a > 15) {
//     console.log('a 가 15 큽니다.');
// } else {
//     console.log('a 가 15보다 크지 않습니다.');
// }
// "a 가 10보다 크지 않습니다."

// IF - ELSE IF 문
// const a = 10;
// if (a === 5) {
//     console.log('5입니다!');
// } else if (a === 10) {
//     console.log('10입니다!');
// } else {
//     console.log('5도 아니고 10도 아닙니다.');
// }
// "10입니다!"

// SWICH / CASE 문
// const device = 'iphone';

// switch (device) {
//     case 'iphone':
//         console.log('아이폰!');
//         break;
//     case 'ipad':
//         console.log('아이패드!');
//         break;
//     case 'galaxy note':
//         console.log('갤럭시 노트!');
//         break;
//     default:
//         console.log('모르겠네요..');
// }

// 함수
// const a = 1;
// const b = 2;
// const sum = a + b;


// function add(a, b) {
//     return a + b;
// }

// const sum = add(1, 2);
// console.log(sum);//3

// function hello(name) {
//     console.log('Hello, ' + name + '!');
// }
// hello('velopert');
// "Hello, velopert!"

// function hello(name) {
//     console.log(`Hello, ${name}!`);
// }
// hello('velopert');

// 화살표 함수
// function 키워드 대신에 => 문자를 사용해서 함수를 구현
// const add = (a, b) => {
//     return a + b;
// };

// console.log(add(1, 2));

// const add = (a, b) => a + b;
// console.log(add(1, 2));

// 객체
// const dog = {
//     name: '멍멍이',
//     age: 2
// };

// console.log(dog.name);
// console.log(dog.age);
// 멍멍이
// 2

// const ironMan = {
//     name: '토니 스타크',
//     actor: '로버트 다우니 주니어',
//     alias: '아이언맨'
// };

// const captainAmerica = {
//     name: '스티븐 로저스',
//     actor: '크리스 에반스',
//     alias: '캡틴 아메리카'
// };

// console.log(ironMan);
// console.log(captainAmerica);
// name: '토니 스타크', actor: '로버트 다우니 주니어', alias: '아이언맨'}
// { name: '스티븐 로저스', actor: '크리스 에반스', alias: '캡틴 아메리카' }


//   함수에서 객체를 파라미터로 받기
// const ironMan = {
//     name: '토니 스타크',
//     actor: '로버트 다우니 주니어',
//     alias: '아이언맨'
// };

// const captainAmerica = {
//     name: '스티븐 로저스',
//     actor: '크리스 에반스',
//     alias: '캡틴 아메리카'
// };

// function print(hero) {
//     const text = `${hero.alias}(${hero.name}) 역할을 맡은 배우는 ${hero.actor} 입니다.`;
//     console.log(text);
// }

// print(ironMan);//아이언맨(토니 스타크) 역할을 맡은 배우는 로버트 다우니 주니어 입니다.
// print(captainAmerica);//캡틴 아메리카(스티븐 로저스) 역할을 맡은 배우는 크리스 에반스 입니다.


//   객체 비구조화 할당
// const ironMan = {
//     name: '토니 스타크',
//     actor: '로버트 다우니 주니어',
//     alias: '아이언맨'
// };

// const captainAmerica = {
//     name: '스티븐 로저스',
//     actor: '크리스 에반스',
//     alias: '캡틴 아메리카'
// };

// function print(hero) {
//     const { alias, name, actor } = hero;
//     const text = `${alias}(${name}) 역할을 맡은 배우는 ${actor} 입니다.`;
//     console.log(text);
// }

// print(ironMan);
// print(captainAmerica);

// 객체 안에 함수 넣기
// const dog = {
//     name: '멍멍이',
//     sound: '멍멍!',
//     say: function say() {
//         console.log(this.sound);
//     }
// };

// dog.say();

//   GETTER 함수와 SETTER 함수
// const numbers = {
//     a: 1,
//     b: 2
// };

// numbers.a = 5;
// console.log(numbers);

// const numbers = {
//     a: 1,
//     b: 2,
//     get sum() {
//         console.log('sum 함수가 실행됩니다!');
//         return this.a + this.b;
//     }
// };

// console.log(numbers.sum);
// numbers.b = 5;
// console.log(numbers.sum);

// const numbers = {
//     _a: 1,
//     _b: 2,
//     sum: 3,
//     calculate() {
//         console.log('calculate');
//         this.sum = this._a + this._b;
//     },
//     get a() {
//         return this._a;
//     },
//     get b() {
//         return this._b;
//     },
//     set a(value) {
//         console.log('a가 바뀝니다.');
//         this._a = value;
//         this.calculate();
//     },
//     set b(value) {
//         console.log('b가 바뀝니다.');
//         this._b = value;
//         this.calculate();
//     }
// };

// console.log(numbers.sum);
// numbers.a = 5;
// numbers.b = 7;
// numbers.a = 9;
// console.log(numbers.sum);
// console.log(numbers.sum);
// console.log(numbers.sum);

// 배열
// const array = [1, 2, 3, 4, 5];

// const objects = [{ name: '멍멍이' }, { name: '야옹이' }];
// console.log(objects);
// console.log(objects[0]);//{name: '야옹이'}
// console.log(objects[1]);//{name: '멍멍이'}

// 배열에 새 항목 추가하기
// const objects = [{ name: '멍멍이' }, { name: '야옹이' }];
// objects.push({
//     name: '멍뭉이'
// })

// console.log(objects);

// 배열의 크기 알아내기
// const objects = [{ name: '멍멍이' }, { name: '야옹이' }];

// console.log(objects.length);//2

// objects.push({
//     name: '멍뭉이'
// });

// console.log(objects.length);//3

// 반복문
// FOR
// for (let i = 0; i < 10; i++) {
//     console.log(i); //1~9
// }


// for (초기 구문; 조건 구문; 변화 구문;) {
//     코드
// }

// for (let i = 10; i > 0; i--) {
//     console.log(i);
// }

// 배열과 FOR
// con3

// FOR...OF
// for...of 문3은 배열에 관한 반복문을 돌리기 위해서 만들어진 반복문

// let numbers = [10, 20, 30, 40, 50];
// for (let number of numbers) { //numbers의 길이 만큼 반복
//     console.log(number);
// }

// 객체를 위한 반복문 FOR..IN
// Object.entries: [[키, 값], [키, 값]] 형태의 배열로 변환
// Object.keys: [키, 키, 키] 형태의 배열로 변환
// Object.values: [값, 값, 값] 형태의 배열로 변환
// const doggy = {
//     name: '멍멍이',
//     sound: '멍멍',
//     age: 2
// };

// console.log(Object.entries(doggy));//[Array(2), Array(2), Array(2)]
// console.log(Object.keys(doggy));//['name', 'sound', 'age']
// console.log(Object.values(doggy));//['멍멍이', '멍멍', 2]

// const doggy = {
//     name: '멍멍이',
//     sound: '멍멍',
//     age: 2
// };

// for (let key in doggy) {
//     console.log(`${key}: ${doggy[key]}`);
// }

// BREAK & CONTINUE
// break 와 continue 를 통하여 반복문에서 벗어나거나, 그 다음 루프를 돌게끔 할 수 있음
// for (let i = 0; i < 10; i++) {
//     if (i === 2) continue; // 다음 루프를 실행
//     console.log(i);
//     if (i === 5) break; // 반복문을 끝내기
// }

// 객체 생성자
// function Animal(type, name, sound) {
//     this.type = type;
//     this.name = name;
//     this.sound = sound;
//     this.say = function () {
//         console.log(this.sound);
//     };
// }

// const dog = new Animal('개', '멍멍이', '멍멍');
// const cat = new Animal('고양이', '야옹이', '야옹');

// dog.say();//멍멍
// cat.say();//야옹

// 프로토타입
// 프로토타입은 다음과 같이 객체 생성자 함수 아래에.prototype.[원하는키] = 코드를 입력하여 설정 할 수 있습니다.
// 객체 생성자를 사용 할 때는 보통 함수의 이름을 대문자로 시작하고, 새로운 객체를 만들 때에는 new 키워드를 앞에 붙여주어야 합니다.
// function Animal(type, name, sound) {
//     this.type = type;
//     this.name = name;
//     this.sound = sound;
// }

// Animal.prototype.say = function () {
//     console.log(this.sound);
// };
// Animal.prototype.sharedValue = 1;

// const dog = new Animal('개', '멍멍이', '멍멍');
// const cat = new Animal('고양이', '야옹이', '야옹');

// dog.say();
// cat.say();

// console.log(dog.sharedValue);
// console.log(cat.sharedValue);

// 객체 생성자 상속받기
// function Animal(type, name, sound) {
//     this.type = type;
//     this.name = name;
//     this.sound = sound;
// }

// Animal.prototype.say = function () {
//     console.log(this.sound);
// };
// Animal.prototype.sharedValue = 1;

// function Dog(name, sound) {
//     Animal.call(this, '개', name, sound);
// }
// Dog.prototype = Animal.prototype;

// function Cat(name, sound) {
//     Animal.call(this, '고양이', name, sound);
// }
// Cat.prototype = Animal.prototype;

// const dog = new Dog('멍멍이', '멍멍');
// const cat = new Cat('야옹이', '야옹');

// dog.say();
// cat.say();

// 클래스
// class 를 사용했을때에는, 다른 클래스를 쉽게 상속 할 수 있습니다.
// class Animal {
//     constructor(type, name, sound) {
//         this.type = type;
//         this.name = name;
//         this.sound = sound;
//     }
//     say() {
//         console.log(this.sound);
//     }
// }

// const dog = new Animal('개', '멍멍이', '멍멍');
// const cat = new Animal('고양이', '야옹이', '야옹');

// dog.say();
// cat.say();

// class Animal {
//     constructor(type, name, sound) {
//         this.type = type;
//         this.name = name;
//         this.sound = sound;
//     }
//     say() {
//         console.log(this.sound);
//     }
// }

// class Dog extends Animal {
//     constructor(name, sound) {
//         super('개', name, sound);
//     }
// }

// class Cat extends Animal {
//     constructor(name, sound) {
//         super('고양이', name, sound);
//     }
// }

// const dog = new Dog('멍멍이', '멍멍');
// const cat = new Cat('야옹이', '야옹');

// dog.say();
// cat.say();

// 상속을 할 때는 extends 키워드를 사용하며, constructor에서 사용하는 super() 함수가 상속받은 클래스의 생성자를 가르킵니다.
// class Animal {
//     constructor(type, name, sound) {
//         this.type = type;
//         this.name = name;
//         this.sound = sound;
//     }
// }

// class Dog extends Animal {
//     constructor(name, sound) {
//         super('개', name, sound);
//     }
// }

// class Cat extends Animal {
//     constructor(name, sound) {
//         super('고양이', name, sound);
//     }
// }

// const dog = new Dog('멍멍이', '멍멍');
// const dog2 = new Dog('왈왈이', '왈왈');
// const cat = new Cat('야옹이', '야옹');
// const cat2 = new Cat('냐옹이', '냐옹');

// dog.say();
// dog2.say();
// cat.say();
// cat2.say();