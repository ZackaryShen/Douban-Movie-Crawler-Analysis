# @Author: Zackary Shen 
# @Date: 2019-06-22 14:41:09  
# @Last Modified by: Zackary Shen  
# @Last Modified time: 2019-06-22 14:41:09  

from matplotlib import pyplot as plt, ticker
import pandas as pd
import operator  # use it to compare string
import matplotlib


class Process_Data:
    """
    This class is to process the source data
    """

    def __init__(self, source_data):
        """
        Get the source data's path, String
        :param source_data:
        """
        self.source_data = source_data

    def Process_init(self):
        """
        Init some data we will use them after
        :return: None
        """
        # read the data from the csv file
        self.data = pd.read_csv(self.source_data)
        self.data = pd.DataFrame(self.data)
        pd.set_option('display.width', None)
        # print(self.data)

        # clean data

        #####################################################################################
        # We need to change the font of matplotlib
        # Or the Chinese char will be error
        # Please change fname to the path of simsun.tff(simsun.ttc in Windows) on your PC
        #####################################################################################
        self.myfont = matplotlib.font_manager.FontProperties(fname='/usr/share/fonts/chinese/TrueType/simsun.ttf')

    def Rank_Type(self):
        """
        To get different types of movies
        And rank the movies group by type
        :return: None
        """

        # use a dict, to store the dataframe of kinds of movies
        self.processed_type = dict()

        # Use list parsing to get all movie types
        self.type_of_movies = []
        for types in self.data['类型']:
            # types is a string, we need to change it to a list
            types = list(types.split(","))
            for i in range(len(types)):
                types[i] = ((types[i].strip('[')).strip(']'))  # clean the "[]"
                types[i] = (types[i].strip("\'")).strip()  # clean the "\'" and space
                types[i] = types[i].lstrip("'")
                self.type_of_movies.append(types[i])

        # use a set, avoid the same types
        self.type_of_movies = set(self.type_of_movies)

        self.has_rank_type = set()
        for i in range(len(self.type_of_movies)):
            # to get all of types movies's info that in a type
            movie_type = list(self.type_of_movies)[i]
            # filter of the null data
            if operator.eq(movie_type, '') is False:
                # append it to has been rank, and
                if movie_type not in self.has_rank_type:
                    self.has_rank_type.add(movie_type)
                    current_type = movie_type

                # create a empty dataframe in the dict
                self.processed_type[current_type] = pd.DataFrame(columns=["地区", "导演", \
                                                                          "时长", "月份", "演员", \
                                                                          "电影名", "类型", \
                                                                          "评分", "评论数", "语言"])

                # if you want to get a row from a dataframe in for rounds
                # you need to use iterrrows(), it returns index and a row
                for ii, tuples in self.data.iterrows():
                    # we need the tuple, so we can append it to the dict
                    mv_type = tuples['类型']
                    mv_type = list(mv_type.split(","))
                    for i in range(len(mv_type)):
                        mv_type[i] = ((mv_type[i].strip('[')).strip(']'))  # clean the "[]"
                        mv_type[i] = (mv_type[i].strip("\'")).strip()  # clean the "\'" and space
                        mv_type[i] = mv_type[i].lstrip("'")
                    for mtype in mv_type:
                        if operator.eq(mtype, current_type) is True:
                            ###########################################################################
                            # You can't just use the append() to append a series to a dataframe
                            # Because the func append() just store the appended dataframe as a copy
                            # you need store the values with "="
                            ###########################################################################
                            self.processed_type[current_type] = self.processed_type[current_type]. \
                                append(tuples, ignore_index=True)

                # print(self.processed_type[current_type])

    def Rank_Region(self):
        """
        To get different region of movies
        And rank the movies group by region
        :return: None
        """

        # use a dict, to store the dataframe of kinds of movies
        self.processed_region = dict()

        # Use list parsing to get all movie original region
        self.region_of_movies = []
        for region in self.data['地区']:
            # types is a string, we need to change it to a list
            region = list(region.split("/"))
            for i in range(len(region)):
                region[i] = ((region[i].strip('[')).strip(']'))  # clean the "[]"
                region[i] = (region[i].strip("\'")).strip()  # clean the "\'" and space
                region[i] = region[i].lstrip("'")
                self.region_of_movies.append(region[i])

        # use a set, avoid the same region
        self.region_of_movies = set(self.region_of_movies)
        # print(self.region_of_movies)

        self.has_rank_region = set()
        for i in range(len(self.region_of_movies)):
            # to get all of region's movies's info that in a type
            movie_region = list(self.region_of_movies)[i]
            # filter of the null data
            if operator.eq(movie_region, '') is False:
                # append it to has been rank, and
                if movie_region not in self.has_rank_region:
                    self.has_rank_region.add(movie_region)
                    current_region = movie_region

                # create a empty dataframe in the dict
                self.processed_region[current_region] = pd.DataFrame(columns=["地区", "导演", \
                                                                              "时长", "月份", "演员", \
                                                                              "电影名", "类型", \
                                                                              "评分", "评论数", "语言"])

                # if you want to get a row from a dataframe in for rounds
                # you need to use iterrrows(), it returns index and a row
                for ii, tuples in self.data.iterrows():
                    # we need the tuple, so we can append it to the dict
                    mv_region = tuples['地区']
                    # get the region of current movie
                    mv_region = list(mv_region.split("/"))
                    for i in range(len(mv_region)):
                        mv_region[i] = ((mv_region[i].strip('[')).strip(']'))  # clean the "[]"
                        mv_region[i] = (mv_region[i].strip("\'")).strip()  # clean the "\'" and space
                        mv_region[i] = mv_region[i].lstrip("'")
                    for mregion in mv_region:
                        if operator.eq(mregion, current_region) is True:
                            ###########################################################################
                            # You can't just use the append() to append a series to a dataframe
                            # Because the func append() just store the appended dataframe as a copy
                            # you need store the values with "="
                            ###########################################################################
                            self.processed_region[current_region] = self.processed_region[current_region]. \
                                append(tuples, ignore_index=True)

                # print(self.processed_region[current_region])

    def Classfiy_By_Published_Time(self):
        """
        To get different publish month of movies
        :return: None
        """
        # use a dict, to store the dataframe of kinds of movies
        self.processed_month = dict()

        # Use list parsing to get all movie month
        self.month_of_movies = []
        # record the total numbers of movies(has same data)
        # use it to calculate the proportion of each month in the pie chart
        self.numbers_of_movies = 0
        for month in self.data['月份']:
            # types is a string, we need to change it to a list
            month = list(month.split(","))
            for i in range(len(month)):
                month[i] = ((month[i].strip('[')).strip(']'))  # clean the "[]"
                month[i] = (month[i].strip("\'")).strip()  # clean the "\'" and space
                month[i] = month[i].lstrip("'")
                month[i] = (month[i])[:2]  # keep only month, not region
                self.month_of_movies.append(month[i])

        # use a set, avoid the same month
        self.month_of_movies = set(self.month_of_movies)

        self.has_rank_month = set()
        for i in range(len(self.month_of_movies)):
            # to get all of month's movies's info that in a type
            movie_month = list(self.month_of_movies)[i]
            # filter of the null data
            if operator.eq(movie_month, '') is False:
                # append it to has been rank, and
                if movie_month not in self.has_rank_month:
                    self.has_rank_month.add(movie_month)
                    current_month = movie_month

                # create a empty dataframe in the dict
                self.processed_month[current_month] = pd.DataFrame(columns=["地区", "导演", \
                                                                            "时长", "月份", "演员", \
                                                                            "电影名", "类型", \
                                                                            "评分", "评论数", "语言"])
                # record the numbers of current month
                self.processed_month[current_month + '_num'] = 0

                # if you want to get a row from a dataframe in for rounds
                # you need to use iterrrows(), it returns index and a row
                for ii, tuples in self.data.iterrows():
                    # we need the tuple, so we can append it to the dict
                    mv_month = tuples['月份']
                    # get the month of current movie
                    mv_month = list(mv_month.split(","))
                    for i in range(len(mv_month)):
                        mv_month[i] = ((mv_month[i].strip('[')).strip(']'))  # clean the "[]"
                        mv_month[i] = (mv_month[i].strip("\'")).strip()  # clean the "\'" and space
                        mv_month[i] = mv_month[i].lstrip("'")
                        mv_month[i] = (mv_month[i])[:2]  # keep only month, not region
                    for mmonth in mv_month:
                        if operator.eq(mmonth, current_month) is True:
                            ###########################################################################
                            # You can't just use the append() to append a series to a dataframe
                            # Because the func append() just store the appended dataframe as a copy
                            # you need store the values with "="
                            ###########################################################################
                            self.processed_month[current_month] = self.processed_month[current_month]. \
                                append(tuples, ignore_index=True)
                            self.processed_month[current_month + '_num'] = self.processed_month[
                                                                               current_month + '_num'] + 1
                            self.numbers_of_movies = self.numbers_of_movies + 1

                # print(self.processed_month[current_month])

    def Ex_Rank_Type(self):
        """
        use the data processed by pandas
        To export a csv that store the movies's rank by type
        :return: None
        """
        for types, movies in self.processed_type.items():
            # Sort the data by movies's credit, and draw it
            movies = movies.sort_values(by='评分', ascending=True)
            # mode='a' means append
            # index=False, do not store the index
            movies.to_csv('/home/zackary/programing/Python/Data_Analysis/Datas/RankByType/' + \
                          types + '电影2018年的排名.csv', mode='a', index=False)

    def Ex_Rank_Region(self):
        """
        use the data processed by pandas
        To export a csv that store the movies's rank by region
        :return: None
        """

        for regions, movies in self.processed_region.items():
            # Sort the data by movies's credit, and draw it
            movies = movies.sort_values(by='评分', ascending=True)
            # mode='a' means append
            # index=False, do not store the index
            movies.to_csv('/home/zackary/programing/Python/Data_Analysis/Datas//RankByRegion/' + \
                          regions + '地区的电影2018年的排名.csv', mode='a', index=False)

    def Draw_Months(self):
        """
        Using the month data of the movie in self
        Draw the distribution time of the movies in each month in current year
        By matplotlib
        :return: None
        """
        ############################################################################
        # self.myfont is definee in self.Process_init(self)
        # It is used to show Chinese correctly
        # useage:fontproperties=self.myfont
        ############################################################################
        result = dict()
        for key, values in self.processed_month.items():
            if operator.eq(key[2:], '_num'):
                result[key[:2]] = (values / self.numbers_of_movies) * 100
        # print(result)

        # use months store key(month), nums to store values
        # we need to store the order
        months = []
        nums = []
        result1 = sorted(result)
        for month in result1:
            months.append(month)
            nums.append(result[month])
        # the pie chart
        fig1, ax1 = plt.subplots()
        ax1.pie(nums, labels=months, autopct='%1.1f%%', shadow=True, startangle=90)
        plt.title('2018年各月份电影上映百分比分布图', fontproperties=self.myfont)

        result2 = dict()
        for key, values in self.processed_month.items():
            if operator.eq(key[2:], '_num'):
                result2[key[:2]] = values
        # use months store key(month), nums to store values
        # we need to store the order
        months = []
        nums = []
        result3 = sorted(result2)
        for month in result3:
            months.append(month)
            nums.append(result2[month])
        # the bar chart
        fig2, ax2 = plt.subplots()
        ax2.bar(months, nums)
        plt.xlabel('月份', fontproperties=self.myfont)
        plt.ylabel('上映电影数', fontproperties=self.myfont)
        plt.title('2018各月份电影上映数量柱状图', fontproperties=self.myfont)

    def Draw_Credit(self):
        """
        Using the credit data of the movie in self
        Draw the proportion of the movies in each range of credit in current year
        By matplotlib"
        :return: None
        """
        ############################################################################
        # self.myfont is definee in self.Process_init(self)
        # It is used to show Chinese correctly
        # useage:fontproperties=self.myfont
        ############################################################################

        #################################################################################
        # average credit by type
        self.credit_by_type_avg = dict()
        self.credit_by_type_total = dict()
        self.numbers_credit_by_type = 0
        for type, dataframe in self.processed_type.items():
            if type != '':
                # get avg credit of each type of movies
                self.credit_by_type_avg[type] = 0
                self.credit_by_type_total[type] = 0
                for index, tuple in dataframe.iterrows():
                    credit = tuple['评分']
                    # Some movies have empty credit
                    if credit != "[\'\']":
                        credit = ((credit.strip('[')).strip(']'))  # clean the "[]"
                        credit = (credit.strip("\'")).strip()  # clean the "\'" and space
                        credit = credit.lstrip("'")
                        credit = int(credit[0])
                        self.credit_by_type_avg[type] = self.credit_by_type_avg[type] + credit
                        self.credit_by_type_total[type] = self.credit_by_type_total[type] + 1
                if self.credit_by_type_total[type] > 0:
                    self.credit_by_type_avg[type] = int(self.credit_by_type_avg[type] / self.credit_by_type_total[type])

        # use the xl to store the x(type), yl store the num
        xl = []
        yl = []
        for type, credit in self.credit_by_type_avg.items():
            if credit > 0:
                xl.append(type)
                yl.append(credit)
        # the bar chart
        fig1, ax1 = plt.subplots()
        # This line is to solve the garbled problem that the source data is Chinese.
        plt.yticks(fontproperties=self.myfont)
        plt.xlabel('平均评分', fontproperties=self.myfont)
        plt.ylabel('类型', fontproperties=self.myfont)
        plt.title('2018各类型电影平均评分柱状图', fontproperties=self.myfont)
        # Draw a horizontal histogram to show more information
        ax1.barh(xl, yl)

        #################################################################################
        # average credit by region
        self.credit_by_region_avg = dict()
        self.credit_by_region_total = dict()
        self.numbers_credit_by_region = 0
        for region, dataframe in self.processed_region.items():
            if region != '':
                # get avg credit of each region of movies
                self.credit_by_region_avg[region] = 0
                self.credit_by_region_total[region] = 0
                for index, tuple in dataframe.iterrows():
                    credit = tuple['评分']
                    # Some movies have empty credit
                    if credit != "[\'\']":
                        credit = ((credit.strip('[')).strip(']'))  # clean the "[]"
                        credit = (credit.strip("\'")).strip()  # clean the "\'" and space
                        credit = credit.lstrip("'")
                        credit = int(credit[0])
                        self.credit_by_region_avg[region] = self.credit_by_region_avg[region] + credit
                        self.credit_by_region_total[region] = self.credit_by_region_total[region] + 1
                if self.credit_by_region_total[region] > 0:
                    self.credit_by_region_avg[region] = int(
                        self.credit_by_region_avg[region] / self.credit_by_region_total[region])

        # use the xl to store the x(type), yl store the num
        xl = []
        yl = []
        for region, credit in self.credit_by_region_avg.items():
            if credit > 0:
                xl.append(region)
                yl.append(credit)
        # the bar chart
        fig2, ax2 = plt.subplots()
        # This line is to solve the garbled problem that the source data is Chinese.
        plt.yticks(fontproperties=self.myfont)
        plt.xlabel('平均评分', fontproperties=self.myfont)
        plt.ylabel('地区', fontproperties=self.myfont)
        plt.title('2018各地区上映的电影平均评分柱状图', fontproperties=self.myfont)
        # Draw a horizontal histogram to show more information
        tick_spacing = 2
        ax2.yaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
        ax2.barh(xl, yl)


if __name__ == '__main__':
    # We must make that the Rank function only run once for each csv file
    # If not, the csv file will be written by same data
    # We just make it show pictures after
    pp = Process_Data('../Datas/SourceData/data1.csv')
    pp.Process_init()
    pp.Rank_Type()
    pp.Rank_Region()
    pp.Classfiy_By_Published_Time()
    pp.Ex_Rank_Type()
    pp.Ex_Rank_Region()
    pp.Draw_Months()
    pp.Draw_Credit()
    plt.show()
