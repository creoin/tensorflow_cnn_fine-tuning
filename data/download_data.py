
import sys
import os.path
import tarfile
from six.moves import urllib
import re

def maybe_download_and_extract(data_url, dest_directory):
  """Download and extract data tar file.

  Args:
    data_url: Web location of the tar file containing the data.
    dest_directory: destination to download to.
  """
  if not os.path.exists(dest_directory):
    os.makedirs(dest_directory)
  filename = data_url.split('/')[-1]
  filepath = os.path.join(dest_directory, filename)
  if not os.path.exists(filepath):

    def _progress(count, block_size, total_size):
      sys.stdout.write('\r>> Downloading %s %.1f%%' %
                       (filename,
                        float(count * block_size) / float(total_size) * 100.0))
      sys.stdout.flush()

    filepath, _ = urllib.request.urlretrieve(data_url, filepath, _progress)
    print()
    statinfo = os.stat(filepath)
    print('Successfully downloaded', filename, statinfo.st_size,
                    'bytes.')
  tarfile.open(filepath, 'r:*').extractall(dest_directory)


data_url = 'http://vision.stanford.edu/aditya86/ImageNetDogs/images.tar'
dest_directory = './ImageNetDogs'

maybe_download_and_extract(data_url, dest_directory)

image_dir = os.path.join(dest_directory, 'Images')
for filename in os.listdir(image_dir):
    label = re.search("(?<=-).+", filename)
    if label:
        newname = label.group(0).capitalize()
        old_path = os.path.join(image_dir, filename)
        new_path = os.path.join(image_dir, newname)
        os.rename(old_path, new_path)
        # print('{:40s} {:40s}'.format(filename, newname))
