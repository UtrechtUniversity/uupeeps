# uupeeps

This package is an interface to public UU employee information. This package was created by Class CoTaPP in live coding session on creating a Python package. 

## Installation

Instal the package with 

```
pip install git+https://github.com/UtrechtUniversity/uupeeps
```

## Usage

Import the package:

```
import uupeeps
```
Get employees per faculty:

```
uupeeps.get_employees_url(5)
```

Get employee info:

```
>>> uupeeps.get_employee_info("ALLamprecht")

{'Guid': '30936d707a9546e6b768c707473c4366', 'Activities': [], 'ActivitiesFreeText': None, 'AdditionalFunctions': None, 'Availability': None, 'Bio': None, 'CV': '<p>Short biography:</p>\n<ul>\n<li>Since 2017: Assistant Professor of Software Technology (here)</li>\n<li>2015 - 2017: Research Fellow at Lero - The Irish Software Research Centre at the University of Limerick, Ireland</li>\n<li>2012 - 2015: Postdoctoral Researcher at the Chair of Service and Software Engineering, Institute of Computer Sciene, University of Potsdam, Germany</li>\n<li>2007 - 2012: PhD Student and Research Assistant at the Chair of Programming Systems, Faculty of Computer Science, TU Dortm

```

## Contact

This package was created by Class CoTaPP in live coding session on creating a Python package. Please contact Jonathan de Bruin for info j.debruin1@uu.nl
