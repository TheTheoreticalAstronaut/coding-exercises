import pytest
from exercises import basic_int as impl

class TestBasicInt:
    def test_init_no_value(self):
        value = 0
        basic_int = impl.BasicInt()
        assert value == basic_int.get(), \
            self._assert_fail_value_str(value, basic_int.get())

    def test_init_positive_value(self):
        value = 7263
        basic_int = impl.BasicInt(value)
        assert value == basic_int.get(), \
            self._assert_fail_value_str(value, basic_int.get())

    def test_init_negative_value(self):
        value = -37
        basic_int = impl.BasicInt(value)
        assert value == basic_int.get(), \
            self._assert_fail_value_str(value, basic_int.get())

    def test_add_positive(self):
        value = 4
        value_op = 12
        basic_int = impl.BasicInt(value)
        basic_int.add(value_op)
        assert (value + value_op) == basic_int.get(), \
            self._assert_fail_value_str(value + value_op, basic_int.get())

    def test_add_negative(self):
        value = -6
        value_op = -9
        basic_int = impl.BasicInt(value)
        basic_int.add(value_op)
        assert (value + value_op) == basic_int.get(), \
            self._assert_fail_value_str(value + value_op, basic_int.get())

    def test_sub_positive(self):
        value = 2
        value_op = -10
        basic_int = impl.BasicInt(value)
        basic_int.sub(value_op)
        assert (value - value_op) == basic_int.get(), \
            self._assert_fail_value_str(value - value_op, basic_int.get())

    def test_sub_negative(self):
        value = -647
        value_op = -1209
        basic_int = impl.BasicInt(value)
        basic_int.sub(value_op)
        assert (value - value_op) == basic_int.get(), \
            self._assert_fail_value_str(value - value_op, basic_int.get())

    def test_mul_positive(self):
        value = 7
        value_op = 8
        basic_int = impl.BasicInt(value)
        basic_int.mul(value_op)
        assert (value * value_op) == basic_int.get(), \
            self._assert_fail_value_str(value * value_op, basic_int.get())

    def test_mul_negative(self):
        value = -2
        value_op = -17
        basic_int = impl.BasicInt(value)
        basic_int.mul(value_op)
        assert (value * value_op) == basic_int.get(), \
            self._assert_fail_value_str(value * value_op, basic_int.get())

    def test_mul_mixed(self):
        value = 6
        value_op = -10
        basic_int = impl.BasicInt(value)
        basic_int.mul(value_op)
        assert (value * value_op) == basic_int.get(), \
            self._assert_fail_value_str(value * value_op, basic_int.get())

    def test_mul_zero(self):
        value = 6817
        value_op = 0
        basic_int = impl.BasicInt(value)
        basic_int.mul(value_op)
        assert (value * value_op) == basic_int.get(), \
            self._assert_fail_value_str(value * value_op, basic_int.get())

    def test_div_positive_exact(self):
        value = 16
        value_op = 4
        basic_int = impl.BasicInt(value)
        basic_int.div(value_op)
        assert (value // value_op) == basic_int.get(), \
            self._assert_fail_value_str(value // value_op, basic_int.get())

    def test_div_positive_inexact(self):
        value = 17
        value_op = 3
        basic_int = impl.BasicInt(value)
        basic_int.div(value_op)
        assert (value // value_op) == basic_int.get(), \
            self._assert_fail_value_str(value // value_op, basic_int.get())

    def test_div_negative_exact(self):
        value = -21
        value_op = -7
        basic_int = impl.BasicInt(value)
        basic_int.div(value_op)
        assert (value // value_op) == basic_int.get(), \
            self._assert_fail_value_str(value // value_op, basic_int.get())

    def test_div_negative_inexact(self):
        value = -20
        value_op = -6
        basic_int = impl.BasicInt(value)
        basic_int.div(value_op)
        assert (value // value_op) == basic_int.get(), \
            self._assert_fail_value_str(value // value_op, basic_int.get())

    def test_div_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            value = 12
            value_op = 0
            basic_int = impl.BasicInt(value)
            basic_int.div(value_op)

    def _assert_fail_value_str(self, expected: int, found: int) -> str:
        return "Unexpected value: expected {0}, found {1}".format(expected, found)
