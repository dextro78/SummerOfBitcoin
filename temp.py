import pandas
import numpy

df = pandas.read_csv('mempool.csv')


df['wbf'] = df.apply(lambda row: row.weight/row.fee, axis=1)

sorted_df = df.sort_values(by='wbf')
sorted_df.to_csv("operations.csv", index=True)

print(df.keys())
print(df['tx_id'])

# result_df = sorted_df

# result_df['new'] = numpy.where(sorted_df['parent'] == '', True, False)

# result_df.to_csv("result.csv", index=True)


file1 = open("output.txt", "w")
file1.write(sorted_df.wbf.to_string(index=True))
file1.close()
