# @Author: Zackary Shen 
# @Date: 2019-06-22 14:41:09  
# @Last Modified by: Zackary Shen  
# @Last Modified time: 2019-06-22 14:41:09  

from matplotlib import pyplot as plt
import pandas as pd
import operator  # use it to compare string


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
            types = types[1:len(types) - 1]  # get rid of "[]" and '\''
            types = list(types.split(","))  # change it to a list
            for i in range(len(types)):
                self.type_of_movies.append(types[i])

        # use a set, avoid the same types
        self.type_of_movies = set(self.type_of_movies)
        # print(self.type_of_movies)

        self.has_rank_type = set()
        for i in range(len(self.type_of_movies)):
            # to get all of types movies's info that in a type
            movie_type = list(self.type_of_movies)[i]

            # append it to has been rank, and
            if movie_type not in self.has_rank_type:
                self.has_rank_type.add(movie_type)
                current_type = movie_type
                pass

                # create a empty dataframe in the dict
                self.processed_type[current_type] = pd.DataFrame(columns=["地区", "导演", \
                                                                          "年份", "时长", "演员", \
                                                                          "电影名", "类型", \
                                                                          "评分", "评论数", "语言"])

            # if you want to get a row from a dataframe in for rounds
            # you need to use iterrrows(), it returns index and a row
            for ii, tuples in self.data.iterrows():
                # we need the tuple, so we can append it to the dict
                mv_type = tuples['类型']
                # get the type of current movie
                mv_type = list((mv_type[1:len(mv_type) - 1]).split(","))
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
            region = region[1:len(region) - 1]  # get rid of "[]" and '\''
            region = list(region.split("/"))  # change it to a list
            for i in range(len(region)):
                self.region_of_movies.append(region[i])

        # use a set, avoid the same region
        self.region_of_movies = set(self.region_of_movies)
        # print(self.region_of_movies)

        self.has_rank_region = set()
        for i in range(len(self.region_of_movies)):
            # to get all of region's movies's info that in a type
            movie_region = list(self.region_of_movies)[i]

            # append it to has been rank, and
            if movie_region not in self.has_rank_region:
                self.has_rank_region.add(movie_region)
                current_region = movie_region
                pass

                # create a empty dataframe in the dict
                self.processed_region[current_region] = pd.DataFrame(columns=["地区", "导演", \
                                                                              "年份", "时长", "演员", \
                                                                              "电影名", "类型", \
                                                                              "评分", "评论数", "语言"])

            # if you want to get a row from a dataframe in for rounds
            # you need to use iterrrows(), it returns index and a row
            for ii, tuples in self.data.iterrows():
                # we need the tuple, so we can append it to the dict
                mv_region = tuples['地区']
                # get the region of current movie
                mv_region = list((mv_region[1:len(mv_region) - 1]).split("/"))
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

    def Ex_Rank_Type(self):
        """
        use the data processed by pandas
        To export a csv that store the movies's rank by type
        :return: None
        """

        for types, movies in self.processed_type.items():
            # Sort the data by movies's credit, and draw it
            movies = movies.sort_values(by='评分', ascending=True)
            movies.to_csv('./Datas/RankByType/' + types + '电影于' + (movies['年份'][0]) + \
                          '年的排名.csv')

    def Ex_Rank_Region(self):
        """
        use the data processed by pandas
        To export a csv that store the movies's rank by region
        :return: None
        """

        for regions, movies in self.processed_region.items():
            # Sort the data by movies's credit, and draw it
            movies = movies.sort_values(by='评分', ascending=True)
            movies.to_csv('./Datas/RankByRegion/' + regions + '地区的电影于' + (movies['年份'][0]) + \
                          '年的排名.csv')


if __name__ == '__main__':
    pp = Process_Data('./Datas/SourceData/source_data.csv')
    pp.Process_init()
    pp.Rank_Type()
    pp.Rank_Region()
    pp.Ex_Rank_Type()
    pp.Ex_Rank_Region()
