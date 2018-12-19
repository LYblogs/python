"""__author__ = 余婷"""

# 提供一个类，功能是给时间和歌名，就可以给你这首歌在这个时间该唱哪句歌词


class Lyrics(object):
    """歌词类"""
    def __init__(self, time: float, text: str):
        self.time = time
        self.text = text.replace('\n', '')

    def __gt__(self, other):#运算符重载
        return  self.time > other.time

    def __repr__(self): #打印对象的时候，返回的是'%.2f:%s' % (self.time, self.text)
        return '%.2f:%s' % (self.time, self.text)


class LyricsAnalyzer(object):
    """歌词解析类"""
    def __init__(self, song: str):
        self.__song = song
        self.__all_lyrics = []

    def __analysis_line(self, line):
        lines = line.split(']')
        # 创建歌词对象
        text = lines[-1]
        for time_str in lines[:-1]:
            fen = float(time_str[1:3])
            miao = float(time_str[4:])
            time = fen * 60 + miao
            lyrics = Lyrics(time, text)
            self.__all_lyrics.append(lyrics)

    def __analysis_file(self):
        """解析歌词文件"""
        # 1.打开歌词文件
        print('打开歌词文件！解析歌词')
        try:
            with open('lyricsFiles/%s.txt' % (self.__song), 'r', encoding='utf-8') as f:
                # b.一行一行的读文件中的内容
                line = f.readline()
                while line:
                    # 在这儿处理文件中每一行的内容
                    self.__analysis_line(line)
                    # 不断读下一行的内容
                    line = f.readline()
        except FileNotFoundError:
            pass

    def get_lyrics(self, time):
        """
        根据时间获取歌词
        :param time: 时间(单位秒)
        :return: 歌词
        """
        if not self.__all_lyrics:
            # 1.解析歌词文件
            self.__analysis_file()
            # 2.根据时间对歌词进行排序
            self.__all_lyrics.sort(reverse=True)
            print(self.__all_lyrics)
            if not self.__all_lyrics:
                return '[没有歌词！]'

            # print(self.__all_lyrics)
        # 3.根据时间找词
        for lyrics in self.__all_lyrics:
            if lyrics.time <= time:
                return lyrics.text


la1 = LyricsAnalyzer('蓝莲花')
print(la1.get_lyrics(10))
print(la1.get_lyrics(30))
print(la1.get_lyrics(20))
print(la1.get_lyrics(100))

la2 = LyricsAnalyzer('夜曲')
print(la2.get_lyrics(40))

