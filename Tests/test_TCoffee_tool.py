# Copyright 2009 by Cymon J. Cox.  All rights reserved.
# This code is part of the Biopython distribution and governed by its
# license.  Please see the LICENSE file that should have been included
# as part of this package.
"""Unittests for Bio.Align.Applications interface for TCOFFEE."""

import sys
import os
import unittest
from cStringIO import StringIO
from Bio import Application
from Bio import AlignIO, SeqIO, MissingExternalDependencyError
from Bio.Align.Applications import TCoffeeCommandline

t_coffee_exe = None
if sys.platform=="win32":
    raise MissingExternalDependencyError(\
        "Testing TCOFFEE on Windows not supported yet")
else :
    import commands
    output = commands.getoutput("t_coffee")
    if "not found" not in output and "t_coffee" in output.lower():
        t_coffee_exe = "t_coffee"

if not t_coffee_exe:
    raise MissingExternalDependencyError(\
        "Install TCOFFEE if you want to use the Bio.Align.Applications wrapper.")

class ProbconsApplication(unittest.TestCase):

    def setUp(self):
        self.infile1 = "Fasta/fa01"
        self.outfile1 = "fa01.aln"
        self.outfile2 = "fa01.html" #Written by default when no output set
        self.outfile3 = "Fasta/tc_out.pir"
        self.outfile4 = "Fasta/tc_out.phy"

    def tearDown(self):
        if os.path.isfile(self.outfile1):
            os.remove(self.outfile1)
        if os.path.isfile(self.outfile2):
            os.remove(self.outfile2)
        if os.path.isfile(self.outfile3):
            os.remove(self.outfile3)
        if os.path.isfile(self.outfile4):
            os.remove(self.outfile4)

    def test_TCoffee_1(self):
        """Round-trip through app and read clustal alignment from file
        """
        cmdline = TCoffeeCommandline(t_coffee_exe, infile=self.infile1)
        self.assertEqual(str(cmdline), t_coffee_exe + " -infile Fasta/fa01")
        stdin, stdout, stderr = Application.generic_run(cmdline)
        self.assertEquals(stdin.return_code, 0)
        self.assertEquals(str(stdin._cl), t_coffee_exe + " -infile Fasta/fa01")
        self.assert_(stderr.read().strip().startswith("PROGRAM: T-COFFEE"))
        align = AlignIO.read(open(self.outfile1), "clustal")
        records = list(SeqIO.parse(open(self.infile1),"fasta"))
        self.assertEqual(len(records),len(align))
        for old, new in zip(records, align) :
            self.assertEqual(old.id, new.id)
            self.assertEqual(str(new.seq).replace("-",""), str(old.seq).replace("-",""))

    def test_TCoffee_2(self):
        """Round-trip through app and read pir alignment from file
        """
        cmdline = TCoffeeCommandline(t_coffee_exe, quiet=True)
        cmdline.infile = self.infile1
        cmdline.outfile = self.outfile3
        cmdline.output = "pir_aln"
        self.assertEqual(str(cmdline), t_coffee_exe + " -output pir_aln "
                    "-infile Fasta/fa01 -outfile Fasta/tc_out.pir -quiet")
        stdin, stdout, stderr = Application.generic_run(cmdline)
        self.assertEquals(stdin.return_code, 0)
        self.assertEquals(stderr.read(), "")
        align = AlignIO.read(open(self.outfile3), "pir")
        records = list(SeqIO.parse(open(self.infile1),"fasta"))
        self.assertEqual(len(records),len(align))
        for old, new in zip(records, align) :
            self.assertEqual(old.id, new.id)
            self.assertEqual(str(new.seq).replace("-",""), str(old.seq).replace("-",""))

    def test_TCoffee_3(self):
        """Round-trip through app and read clustalw alignment from file
        """
        cmdline = TCoffeeCommandline(t_coffee_exe, gapopen=-2)
        cmdline.infile = self.infile1
        cmdline.outfile = self.outfile4
        cmdline.set_parameter("output", "clustalw_aln")
        cmdline.outorder = "input"
        cmdline.set_parameter("gapext", -5)
        cmdline.type = "protein"
        self.assertEqual(str(cmdline), t_coffee_exe + " -output clustalw_aln "
                         "-infile Fasta/fa01 -outfile Fasta/tc_out.phy "
                         "-outorder input -gapopen -2 -gapext -5")
        stdin, stdout, stderr = Application.generic_run(cmdline)
        self.assertEquals(stdin.return_code, 0)
        self.assert_(stderr.read().strip().startswith("PROGRAM: T-COFFEE"))
        align = AlignIO.read(open(self.outfile4), "clustal")
        records = list(SeqIO.parse(open(self.infile1),"fasta"))
        self.assertEqual(len(records),len(align))
        for old, new in zip(records, align) :
            self.assertEqual(old.id, new.id)
            self.assertEqual(str(new.seq).replace("-",""), str(old.seq).replace("-",""))

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity = 2)
    unittest.main(testRunner=runner)
