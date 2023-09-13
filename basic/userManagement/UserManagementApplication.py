# from userManagement.view.ClearView import clear
def main():
    from userManagement.view.MenuView import MenuView # 변수만 가져오는 것도 가능
    while(MenuView.index()):
        # clear()
        pass

if __name__ == "__main__":
    main()
    print("프로그램이 종료되었습니다.")