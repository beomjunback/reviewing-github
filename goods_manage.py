# 재고 관리 심화버전을 더 심화시킬 예정
# 방법: 기존 재고 관리 심화버전에서 사용자의 예산까지 고려하는 프로그램을 내가 아는코드로 만들어 본다.

dictgoods = {'바나나':2 , '사과':3 , '복숭아':4}
price = {'바나나':1200 , '사과':900 , '복숭아':1400 , '배':900 , '포도':1400 , '귤':100 , '수박':9000 , '딸기':120}
money = 20000
can = (price.keys() - dictgoods.keys())
print("재고 관리, 조사 프로그램 입니다.")
    
def jaego():
    print(goods,"의 재고는",dictgoods[goods],"개 입니다.")

def mistake():
    print("알맞은 숫자/번호/이름 (을)를 입력하세요")

print("당신의 현재 자산은",money,"원 입니다")

while True:

    ch = int(input("(1)재고 조사 , (2)재고 관리 , (3)새 제품 주문 , (4)자산 보기 , (5)종료 = "))

    if ch == 1: #재고조사

        print("현재 보유하신 상품은:",dictgoods,"입니다.")
        

    elif ch == 2: #재고관리

        while True:
            print("현재 보유하신 상품은:",dictgoods,"입니다.")
            goods = input("관리를 원하시는 상품을 입력해주세요/뒤로가기를 원하시면 '종료'를 입력하세요 : ")

            if goods in dictgoods:

                while True:

                    jaego()
                    ch2 = int(input("(1)추가 , (2)판매 , (3)종료 : "))



                    if ch2 == 1: #구매

                        while True:
                            
                            print("당신의 현재 자산은",money,"원 입니다")
                            want = goods

                            if want in dictgoods:
                                print(want,"는 개당",price[want],"원 입니다")
                                hm = int(input("몇 개 구입 하시겠습니까? : "))

                                if hm > 0:

                                    to = price[want] * hm

                                    if to <= money: #돈이 충분
                                        print("총",to,"원 입니다")
                                        ans = input("구매 하시겠습니까? [yes/no] : ")

                                        if ans == "yes":
                                            money = money - to
                                            dictgoods[want] = dictgoods[want] + hm
                                            print("구매 완료")
                                            break
                                            
                                        elif ans == "no":
                                            break
                                        else:
                                            mistake()

                                    elif to > money: # 돈이 부족
                                        print("돈이 부족합니다")
                                        
                                else:
                                    mistake()
                                    
                            elif want == "종료":
                                break

                            else:
                                mistake()
                            

                    elif ch2 == 2: #판매

                        while True:
                            
                            want = goods

                            if want in dictgoods:
                                hm = int(input("몇 개 판매 하시겠습니까? : "))

                                if hm > 0 and hm <= dictgoods[want]:

                                    to = price[want] * hm
                                    print("총",to,"원 입니다")
                                    ans = input("판매 하시겠습니까? [yes/no] : ")

                                    if ans == "yes":
                                        money = money + to
                                        dictgoods[want] = dictgoods[want] - hm
                                        if dictgoods[want] == 0:
                                            dictgoods.pop(want)
                                        print("판매 완료")
                                        break
                                            
                                    elif ans == "no":
                                        break
                                    else:
                                        mistake()
                                        
                                else:
                                    mistake()
                                    
                            elif want == "종료":
                                break

                            else:
                                mistake()

                        break

                    elif ch2 == 3: #종료

                        break

                    else: # 잘못된 입력

                        mistake()

            elif goods == "종료":

                break

            else: #잘못된 입력

                mistake()





    elif ch == 3: #새 제품 주문

        while True:
            can = (price.keys() - dictgoods.keys())
            print("구매가능상품:", can)
            print("당신의 현재 자산은",money,"원 입니다")
            want = input("구매하고자 하는 상품을 입력하세요./뒤로 가기를 원하시면 '종료'를 입력하세요.:")

            if want in can:
                print(want,"는 개당",price[want],"원 입니다")
                hm = int(input("몇 개 구입 하시겠습니까? : "))

                if hm > 0:

                    to = price[want] * hm

                    if to <= money: #돈이 충분
                        print("총",to,"원 입니다")
                        ans = input("구매 하시겠습니까? [yes/no] : ")

                        if ans == "yes":
                            money = money - to
                            dictgoods[want] = hm
                            print("구매 완료")
                            
                                            
                        elif ans == "no":
                            break
                        else:
                            mistake()

                    elif to > money: # 돈이 부족
                        print("돈이 부족합니다")
                                        
                else:
                    mistake()
                                    
            elif want == "종료":
                break

            else:
                mistake()

    elif ch == 4: #자산

        print("당신의 현재 자산은",money,"원 입니다")

    elif ch == 5: #종료

        break
    
    else: #잘못된 답변

        mistake()

    
print("당신의 현재 자산은",money,"입니다")
print("보유 상품:", dictgoods)
print("프로그램 종료")
