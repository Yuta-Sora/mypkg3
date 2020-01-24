# mypkg3
このパッケージは、ROS上でパブリッシャから入力した文字をサブスクライバ側で表示できるプログラムです。  
また、パブリッシャ側で打ち込んだ２つの数字の和、または差を求めることもできます。
## 機能紹介    
このプログラムには5つの機能があります。  
1.送信回数のカウント  
2.送信ごとに Hello World を送信  
3.入力文字をサブスクライバ側で表示  
4.2つの数の和をサブスクライバ側で表示  
5.2つの数の差をサブスクライバ側で表示  
## 使い方  
パブリッシャ側ノード:count.py  
サブスクライバ側ノード:twice.py  
1.ROSのインストールされたUbuntu端末を用意する  
2.roscore でROSを実行  
3.端末画面で cd ~/catkin_ws/src と入力  
　又は任意のワークスペース/srcへ移動  
4.このリポジトリを git clone する  
5.ワークスペース（cd ~/catkin_ws)へ移動し catkin_make を実行  
6.rosrun mypkg3 count.py  
　rosrun mypkg3 twice.py  
  をそれぞれ別の端末で実行  
7.count.py側で  
    ・1.文字入力 + Enter で　twice.py側に入力した文字が表示される  
    ・2.<+> を入力後指示に従って数値を打つと　tiwce.py側で入力された式と答えが表示される（和）  
    ・3.<-> を入力後指示に従って数値を打つと　tiwce.py側で入力された式と答えが表示される（差）  
    ・4.rostopic echo /count_up で送信回数が表示される  
    ・5.rostopic echo /count_2 で送信毎に Hello World が表示される  
##デモ動画  
https://www.youtube.com/watch?v=N04XVfgjIwE
## License  
This software is released under the BSD 2-Clause "Simplified" License, see LICENSE.
