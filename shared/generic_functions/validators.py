import re

REGEX_CPF_CNPJ = r'^(\d{11}|\d{14})$'


class Validators:

    @classmethod
    def validate_cpf(cls, cpf: str) -> bool:
        """Validates a CPF number.

        Args:
            cpf (str): The CPF number to validate.

        Returns:
            bool: True if the CPF number is valid, False otherwise.
        """

        x = re.search(
            r'^[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2}$',
            cpf
        )

        if x:
            return True
        return False

    @classmethod
    def validate_cnpj(cls, cnpj: str) -> bool:
        """Validates a CNPJ number.

        Args:
            cnpj (str): The CNPJ number to validate.

        Returns:
            bool: True if the CNPJ number is valid, False otherwise.
        """

        x = re.search(r'^[0-9]{2}\.?[0-9]{3}\.?[0-9]{3}\/?[0-9]{4}\-?[0-9]{2}$', cnpj)

        if x:
            return True
        return False
