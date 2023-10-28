import os
import sys
from dataclasses import dataclass

VERBOSE = True


class out:
    """Output printing utility class"""

    def err(*args):
        """Wrapper for print that adds an error prefix"""
        print(f"\033[91m\033[1merror\033[0m: ", end="")
        print(*args)

    def warn(*args):
        """Wrapper for print that adds a warning prefix"""
        print(f"\033[93m\033[1mwarning\033[0m: ", end="")
        print(*args)

    def info(*args):
        """Wrapper for print that adds an info prefix"""
        print(f"\033[94m\033[1minfo\033[0m: ", end="")
        print(*args)


@dataclass
class PdfData:
    """Utility dataclass for storing PDF information
    `data: bytes` - the raw PDF bytes
    `header: bytes` - the header (first line) of the PDF
    `size: int` - the size of the PDF file
    """

    data: bytes
    header: bytes
    size: int

    def __str__(self):
        props = ""
        for key in self.__dataclass_fields__:
            value = self.__getattribute__(key)
            if type(value) is bytes or type(value) is str:
                props += (
                    f"\n\t{key}:\t{ value if len(value) <= 16 else f'{value[:16]}...'}"
                )
            elif type(value) is int or type(value) is float:
                props += f"\n\t{key}:\t{value:,}"
            else:
                props += f"\n\t{key}:\t{value}"
        return f"{self.__class__.__name__}({props}\n)"


if len(sys.argv) < 2:
    out.err("no input PDF specified")
    exit(1)
elif len(sys.argv) < 3:
    out.err("no output PDF specified")
    exit(1)
elif len(sys.argv) < 4:
    out.err("no new PDF size specified")
    exit(1)

# Try to read PDF

try:
    pdf = open(sys.argv[1], "rb")
    data = pdf.read()
    pdf_data = PdfData(
        data=data,
        header=data[: data.index(b"\n")],
        size=os.path.getsize(sys.argv[1]),
    )
    pdf.close()
except Exception as e:
    out.err(str(e))
    exit(1)

if int(sys.argv[3]) <= pdf_data.size:
    out.err(
        f"PDF size ({pdf_data.size}) is more than to new PDF size ({int(sys.argv[3])})"
    )
    exit(1)

print(pdf_data)

# Insert filler bytes as a comment in the trailer of the PDF

if float(pdf_data.header[5:]) < 1.2:
    out.err("PDF version less than 1.2 not supported")
    exit(1)
elif VERBOSE:
    out.info(f"PDF version {pdf_data.header[5:].decode()} supported")

trailer_section = pdf_data.data.find(b"trailer")
trailer_start = pdf_data.data[trailer_section:].find(b"<<") + trailer_section + 2
trailer_end = pdf_data.data[trailer_section:].find(b">>") + trailer_section
if trailer_section == -1:
    out.warn("no trailer found; creating artifical trailer...")
    out.err("artifical trailer not implemented yet")
    exit(1)
else:
    insert_size = int(sys.argv[3]) - pdf_data.size

    new_pdf_data = (
        pdf_data.data[:trailer_start]
        + b"%"
        + b"L" * (insert_size - 2)
        + b"\n"
        + pdf_data.data[trailer_start:]
    )

    if VERBOSE:
        out.info(
            f"trailer found at {trailer_section}; data is at {trailer_start}:{trailer_end} ({pdf_data.data[trailer_start-2:trailer_start].decode()}...{pdf_data.data[trailer_end:trailer_end+2].decode()})"
        )
        out.info(f"trailer data: {pdf_data.data[trailer_start:trailer_end]}")
        out.info(f"inserting {insert_size} bytes into trailer...")
        out.info(f"successfully inserted; new size of PDF is {len(new_pdf_data)}")

# Save the new PDF

try:
    pdf = open(sys.argv[2], "wb")
    pdf.write(new_pdf_data)
    pdf.close()
except Exception as e:
    out.err(str(e))
    exit(1)

if VERBOSE:
    out.info("successfully wrote to PDF")
