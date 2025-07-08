# break using for
for i in range(10):
  if i == 5:
    break
  print(i)

  # continue using for
  print("-----------")
  for i in range(10):
    if i == 5:
      continue
    print(i)