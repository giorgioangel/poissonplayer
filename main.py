#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2021 Giorgio Angelotti
#
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import subprocess
import numpy as np
import os
from scipy.stats import expon
from time import sleep

def list_files(dir):
    lista = []
    for file in os.listdir(dir):
        if file.endswith('.mp3'):
            lista.append(r''+os.path.join(dir, file))
    return lista




def random_file(lista):
    index = np.random.randint(0, len(lista))
    return lista[index]


if __name__ == '__main__':
    directory = 'sounds/'
    suoni = list_files(directory)
    while True:
        suono = random_file(suoni)
        rv = expon.rvs(scale = 0.3)
        subprocess.run(['vlc', suono,
                        '--play-and-exit'])
        print("Riprodotto " + suono + " , ora aspetto " + str(np.around(rv, decimals=3)) + " minuti.")
        sleep(rv*60)