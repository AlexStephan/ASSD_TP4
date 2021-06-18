from src.backend2.filter_writer import FilterWriter
if __name__ == '__main__':
    filter_writer = FilterWriter()
    if filter_writer.save_file(".\\resources\\csv\\OBAMATI5000.csv",[[0,1,1,2],[5,7,3,6]]):
        print("YES")