# (尝试)5.写一个类，其功能是：1.解析指定的歌词文件的内容 2.按时间显示歌词
# 提示：歌词文件的内容一般是按下面的格式进行存储的。
# 歌词前面对应的是时间，在对应的时间点可以显示对应的歌词


# 1 时间
# 2 文件
# 创建歌词对象
# 解析歌词文件"
# 根据时间获取歌词
class Lyrics(object):
    """歌词类"""
    def __init__(self,time,text):
        self.time =time #歌词时间
        self.text =text #歌词内容
    def __repr__(self): #打印对象返回值
        return "%.2f:%s"%(self.time,self.text)
    def __lt__(self, other): #运算符重载
        return self.time <other.time


class LyricsAnalysis(object):
    def __init__(self,song):
        self.song_name =song
        self.all_lyrics =[]


    def analysis_line(self,line):
        """
        解析歌词
        :param line:
        :return:
        """
        nuw_line = line.split("]")
        text = nuw_line[-1]
        for time in nuw_line[:-1]:
            fen = float(time[1:3])
            miao = float(time[4:])
            time = fen * 60 + miao
            lyrcis1 = Lyrics(time, text)
            self.all_lyrics.append(lyrcis1)


    def analyze_files(self):
        """
        解析歌词文件
        :return:
        """
        try:
            with open("lyzer/%s.txt"%self.song_name,"r",encoding="utf-8")as f:
                line =f.readline()
                while line:
                    self.analysis_line(line)
                    line = f.readline()
        except FileNotFoundError:
            pass

    def get_lyrics(self,time):
        if not self.all_lyrics:
            self.analyze_files()
            self.all_lyrics.sort(reverse=True)
            if not self.all_lyrics:
                return "没有歌词"
        for lyrics1 in self.all_lyrics:
            if lyrics1.time<=time:
                return lyrics1.text

if __name__ == "__main__":
    l1 =LyricsAnalysis("蓝莲花")
    print(l1.get_lyrics(10))
    l2 =LyricsAnalysis("夜曲")
    print(l2.get_lyrics(20))