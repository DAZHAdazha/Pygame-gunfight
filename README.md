# Pygame——Gun Fight

> * level: middle-

> * techniques: pygame library based on python

> * develop reason: one day I suddenly want to play a game when I was young, but I can not think of its name, so I just strat to create my own version

> * my gain:
> A practice project when I study python myself
>  My first time to use a lot of "Class", inheritance and other OOP features
>  And I start to know how to use pygame by adding images, music, and basic physical system build by myself(velocity, accelerate velocity, collision, recoil force...)
>  
> * deficiencies:
>   * because of the pygame-limitations, a lot of new functionalities that I would like to add could not be implemented, such as multiple sound effects(pygame only support single BGM)
>   * Because of the pygame performance limitation(or my poor programming skills :( ), the background pictures will lead to low fps situation, so there is only a black background in the back
>   * Because this is my first time to use OOP, so the code is totally a mess, and there are many code redundancy, I was intended to add multiple weapans, skill systems, but I was too lazy to add...
>   * The original movement, coliision system is a totally **disaster**, and according to my friends who gave me a hint about using real world physics system, then everythings were clear and straight, though the code is still a mess :(...

## About the game

> * I was intended to develop a double players gun fight plus single player version. However, I do not know how to build an AI at that time...
> * how to play:
>   * player1: wasd to move,g to attck which will use a sword to dash, with 2 seconds cooldown and if you hit enemy in a short distance, enemy will be pushed back.
>   * player2: ←↑↓→ to move, l to attack, which will use a pistol to shot, only three bullets could be appeared in screen, pistol has small recoil force, bullets could also push enemy consistently.
>   * w and ↑ are j jetpack system, if you push the key and hold then you could fly, and you also could double jump.
>   * death: if you are exceed the left and right boundary for 2 seconds then you die(there are counter on the screen) if you touch the strikes in the upper and lower boundary you will also be dead.

# Pygame小游戏——自制版混乱大枪战

> * 难度：中等-

> * 应用技术：利用python 基于pygame第三方库制作的小游戏

> * 开发原因：有天心血来潮想玩玩小时候玩的一款4399小游戏，但是又暂时想不起名字，于是便决定自己做一个自（~~山~~)制(~~寨~~)版
> * （虽然做好后又想起了这款游戏叫做《混乱大枪战》...( ＿ ＿)ノ｜ 而且人物样子还是用的百战天虫的???(っ °Д °;)っ

> * 主要收获：早期学习python过程中的一个练手项目，第一次尝试大量运用类，继承等OOP特性进行开发，并且逐渐熟悉了pygame库的使用，在游戏中加入了图片，音乐，以及最基础的物理系统（速度，加速度，碰撞，后坐力等）

> * 不足：
>   * 由于pygame第三方库的限制，许多想加入的功能只好放弃，比如原本考虑增加的射击、击中音效由于pygame只有应用于BGM的单音轨，只好放弃。
>   * 由于pygame性能限制，导致插入背景图片会非常卡顿，所以只好再次沿用简陋的“纯黑”背景（当然也可能是我自己太弱不知道如何优化(；′⌒`)
>   * 鉴于第一次大量使用类，导致写的非常混乱，各种继承乱七八糟，而且也没有很好的体现出类的可复用性，反而使代码异常繁杂，原本打算加入的多武器、技能等系统的加入或许会让类显得更加高效，但是由于种种原因（~~懒~~）而一直搁置，不知道以后会不会想起来慢慢更新吧，以后也应该好好多加强类的使用呜呜呜
>   * 原本写的移动、碰撞系统简直糟糕的一塌糊涂，但是由于别人的提醒想到使用现实物理中的速度、加速度等概念一下子变得流畅、明朗了好多，看来自己以后也应当思维更加开阔才行欸

## 关于游戏

> * 原本打算开发双人对战模式以及单人闯关模式，但是由于时间因素，以及对如何写AI的不熟练（~~其实还是懒~~）于是只写出来简陋的双人模式...
> * 游戏操作：
>   * player1: wasd控制方向，g为攻击键，提起大剑发起冲锋，有2s的冷却，在近距离冲撞到敌人会将敌人击飞
>   * player2: ←↑↓→对应方向键，l为攻击键，使用手枪发出子弹，子弹只能在屏幕中存在3颗，手枪有一点后坐力，击中敌人会将其持续击飞
>   * w键和↑键为喷气背包跳跃（虽然没有喷气效果o(*￣▽￣*)o）持续按住可以飞高，可在空中二连跳，但是要小心上方尖刺哦
>   * 死亡判定：连续超出左右屏幕2s会造成死亡（在屏幕上会有提示）碰触到上下方的尖刺也同样会造成死亡

![images](https://github.com/DAZHAdazha/Pygame-gunfight/blob/master/images/1.png)

![images](https://github.com/DAZHAdazha/Pygame-gunfight/blob/master/images/2.png)

![images](https://github.com/DAZHAdazha/Pygame-gunfight/blob/master/images/3.jpg)

![images](https://github.com/DAZHAdazha/Pygame-gunfight/blob/master/images/4.jpg)
