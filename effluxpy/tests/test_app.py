import os
import os.path
import unittest
import tempfile

import effluxpy
import effluxpy.appconfig


class TestApp(unittest.TestCase):
    module = effluxpy
    app = effluxpy.app

    def test_config(self):
        try:
            with tempfile.NamedTemporaryFile(delete=False) as f:
                f.write(b'DIRECTORY_DOWNLOADABLE = False\n')
                name = f.name
            os.environ['effluxpy_TEST_SETTINGS'] = name
            self.app.config['directory_downloadable'] = True
            self.app.config.from_envvar('effluxpy_TEST_SETTINGS')
            self.assertFalse(self.app.config['directory_downloadable'])
        finally:
            os.remove(name)


class TestConfig(unittest.TestCase):
    pwd = os.path.dirname(os.path.abspath(__file__))
    module = effluxpy.appconfig

    def test_case_insensitivity(self):
        cfg = self.module.Config(self.pwd, defaults={'prop': 2})
        self.assertEqual(cfg['prop'], cfg['PROP'])
        self.assertEqual(cfg['pRoP'], cfg.pop('prop'))
        cfg.update(prop=1)
        self.assertEqual(cfg['PROP'], 1)
        self.assertEqual(cfg.get('pRop'), 1)
        self.assertEqual(cfg.popitem(), ('PROP', 1))
        self.assertRaises(KeyError, cfg.pop, 'prop')
        cfg.update(prop=1)
        del cfg['PrOp']
        self.assertRaises(KeyError, cfg.__delitem__, 'prop')
        self.assertIsNone(cfg.pop('prop', None))
        self.assertIsNone(cfg.get('prop'))
