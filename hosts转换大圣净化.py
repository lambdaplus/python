#!/usr/bin/env python
# coding: utf-8

# In[32]:


with open('/home/lambda/Downloads/host.html', 'r') as f:
    new_f = open('/home/lambda/Downloads/ad.yaml', 'w')
    new_f.write('hosts:\n')
    new_f.write('  router.asus.com: 192.168.50.1\n')
    new_f.write('  services.googleapis.cn: 74.125.193.94\n')
    for lines in f:
        if '#' not in lines and not lines == "\n":
            tail = lines[9:].strip()
            head = lines[:9].strip()
            new_lines = "  " + tail + ": " + head
            new_f.write(new_lines+'\n')
        else:
            pass
    new_f.close()


# In[ ]:




