from .context import *
from Problems.Fonseca import Fonseca
from Problems.Constrex import Constrex
from Problems.Schaffer import Schaffer
from Friendly_Errors import DecisionOutOfBoundsError, NullInputError, ImproperInputError
import unittest


class TestProblems(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass
        
    def _try_common_error_cases(self, problem):
        """make sure the problem raises an issue with decisions being out of bounds"""
        prob = problem()
        num_variables = len(prob.decision_variables)
        first_var_upper_bound = prob.decision_variables[0].upper_bound
        self.assertRaises(DecisionOutOfBoundsError, prob.evaluate, input = [first_var_upper_bound+1 for i in range(num_variables)])

        """make sure the problem raises an issue with no input on evaluation call"""
        self.assertRaises(NullInputError, prob.evaluate)

        """make sure problem raises an issue if evaluation input has wrong length"""
        self.assertRaises(ImproperInputError, prob.evaluate, input = [first_var_upper_bound for i in range(num_variables+1)])

    def test_schaffer(self):
        """Ensure that then Schaffer problem is working properly"""
        self.assertEquals(abs(Schaffer(boundary=2).decision_variables[0].lower_bound), Schaffer(boundary=2).decision_variables[0].upper_bound, 2)
        self.assertEquals(Schaffer().evaluate(input = [7]), [49,25])
        self._try_common_error_cases(Schaffer)
        self.assertRaises(ImproperInputError, Schaffer().__init__, boundary = 'a')
           
    def test_fonseca(self):
        """Ensure that then Schaffer problem is working properly"""
        self.assertEquals(Fonseca().evaluate(input = [1,1]), [0.15766111987646092, 0.9970572981549862])
        self.assertEquals(len(Fonseca(num_variables=5).decision_variables), 5)
        self.assertEquals(abs(Fonseca(boundary=2).decision_variables[0].lower_bound), Fonseca(boundary=2).decision_variables[0].upper_bound, 2)
        self.assertEquals(Fonseca(num_variables=5).evaluate(input = [1,1,1,1,1]), [0.7830013279401842, 0.9999716854840861])
        self._try_common_error_cases(Fonseca)
        self.assertRaises(ImproperInputError, Fonseca().__init__, boundary = 'a')
        self.assertRaises(ImproperInputError, Fonseca().__init__, num_variables = 1.1)
        self.assertRaises(ImproperInputError, Fonseca().__init__, num_variables = 'a')

    def test_constrex(self):
        """Ensure that then Constrex problem is working properly"""
        self.assertEquals(Constrex().evaluate(input = [1,5]), [1,6])
        self.assertGreaterEqual(Constrex().decision_variables[0].lower_bound, 0.1)
        self.assertGreaterEqual(Constrex().decision_variables[1].lower_bound, 0)
        self.assertLessEqual(Constrex().decision_variables[0].upper_bound, 1.0)
        self.assertLessEqual(Constrex().decision_variables[1].upper_bound, 5)
        self._try_common_error_cases(Constrex)
        self.assertTrue(Constrex().evaluate_constraints(input = [1,5]))
        self.assertFalse(Constrex().evaluate_constraints(input = [0.5,1]))

if __name__ == '__main__':
    unittest.main()
