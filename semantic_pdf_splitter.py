import luigi
import glob
import requests
import os

from extractor import processPDF


class ProcessPDF(luigi.Task):

    f = luigi.Parameter()
    fout = luigi.Parameter()

    def run(self):
        processPDF(self.f, self.fout)
        with self.output().open('w') as out_file:
            out_file.write(self.f)

    def output(self):
        return luigi.LocalTarget('data/%s.txt' % os.path.basename(self.f))


class GetFiles(luigi.Task):

    fin = luigi.Parameter()
    fout = luigi.Parameter()

    def requires(self):
        files = glob.glob(self.fin + '/*.pdf')
        return [ProcessPDF(f, self.fout) for f in files]

    def run(self):
        pass

if __name__ == "__main__":
    luigi.run()
