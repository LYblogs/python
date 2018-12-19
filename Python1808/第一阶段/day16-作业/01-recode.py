"""
1.文件操作和异常捕获
2.面向对象
a.类的声明
class  类名：
    类的方法
    类的属性

b.创建对象
变量名 = 类名（）

c.方法
对象方法
python 中 所有的类都是直接或者间接继承object的
继承，子类会继承父类所有的属性和方法

运算符重载：在类中实现相应的魔法方法，让类的对象能够支持相应的运算符


"""
class Lyrics:
    def __init__(self,time,text):
        """歌词类"""
        self.time =time
        self.text =text
    def __lt__(self, other):
        return self.time<other.time
    def __repr__(self):
        return "%.2f:%s"%(self.time,self.text)


class  LyicsAnalyzer(object):
    def __init__(self,song):
        self.song_name=song
        self.all_lyrics =[]
    def analysis_line(self,line):
        # 在这处理文件中的内容
        lines = line.split("]")
        # 创建歌词对象
        text = lines[-1]
        for time_str in lines[:-1]:
            # print(time_str)
            fen = float(time_str[1:3])
            miao = float(time_str[4:])
            time = fen * 60 + miao
            lyrics = Lyrics(time, text)
            self.all_lyrics.append(lyrics)
    def __analysis_file(self):
        try:
            with open("lyzer/%s.txt"%self.song_name,"r",encoding="utf-8") as f:
                #一行一行的读文件中的内容
                line =f.readline()
                while line:
                    self.analysis_line(line)
                    # print(line)
                    line  =f.readline()
        except FileNotFoundError:
            pass
    def get_lyrics(self,time):
        """
        获取时间获取歌词
        :param time: 时间
        :return: 歌词
        """
        if not self.all_lyrics:
            self.__analysis_file()
            self.all_lyrics.sort(reverse=True)
            if self.all_lyrics == []:
                return "没有歌词"
            # print(self.all_lyrics)
        for lyrics in self.all_lyrics:
            if lyrics.time <=time:
                return lyrics.text

ly1 =LyicsAnalyzer("蓝莲花")
print(ly1.get_lyrics(30))
print(ly1.get_lyrics(50))
ly2 =LyicsAnalyzer("夜曲")
print(ly2.get_lyrics(30))