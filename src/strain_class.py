# Class holds useful information! nice! This will probably change at some point.
class DnaData:
  def __init__(self, name, date):
    self.name = name
    self.date = date
    self.segments = {}

  def __str__(self):
    output = ''
    output += f'Isolate name, Collection date: {self.name} | {self.date}\n'
    for seg_name, seg_data in self.segments.items():
        output += f'-{seg_name}\n'
        output += f'{seg_data}\n'
    return output
