## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>.
##

from struct import pack, unpack
from random import randbytes
from glob import glob


class Util(object):
    @staticmethod
    def write_bin(filename, data):
        with open(filename, "wb") as f:
            f.write(data)

    @staticmethod
    def read_bin(filename):
        data = None
        with open(filename, "rb") as f:
            data = f.read()
        return data

    @staticmethod
    def word2bytes(word):
        result=[(word)&0xff,(word>>8)&0xff,(word>>16)&0xff,(word>>24)&0xff]
        return bytes(result)

    @staticmethod
    def pack_res(filename, dir_="res/"):
        print("pack...")
        with open(filename, "wb") as fout:
            data = {}
            for fname in glob(f"{dir_}/*/*"):
                with open(fname, "rb") as f:
                    data.update({fname: f.read()})
                fout.write(fname.encode())
                fout.write(pack("<c", b';'))
            fout.write(pack("<c", b';'))

            imax = 0
            for k in data:
                sz = len(data[k])
                fout.write(pack("<i", sz))
                fout.write(pack("<c", b';'))
                if sz > imax:
                    imax = sz
            for i in range(imax):
                for k in data:
                    if i < len(data[k]):
                        fout.write(data[k][i:i+1])
                    else:
                        fout.write(randbytes(1))

    @staticmethod
    def unpack_res(filename):
        print("unpack...")
        with open(filename, "rb") as fin:
            files = []
            sizes = []
            while 1:
                s = " "
                while s[-1] != ';':
                    s += unpack("<c", fin.read(1))[0].decode()
                if s[1:-1] == "":
                    break
                files += [s[1:-1]]
            while 1:
                i = unpack("<i", fin.read(4))[0]
                c = unpack("<c", fin.read(1))[0]
                if c != b';':
                    fin.seek(-5, 1)
                    break
                sizes += [i]
            data = {}
            assert len(files) == len(sizes), files
            for f, s in zip(files, sizes):
                data.update({f: bytearray(s)})

            for i in range(max(sizes)):
                for k in data:
                    b = fin.read(1)
                    if b == b'':
                        break
                    if i < len(data[k]):
                        data[k][i:i+1] = b
                if b == b'':
                    break

            return data


if __name__ == "__main__":
    Util.pack_res("res.pack")
    data = Util.unpack_res("res.pack")
