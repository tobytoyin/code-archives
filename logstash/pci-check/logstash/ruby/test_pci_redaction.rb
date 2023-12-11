require 'minitest/autorun'
require_relative 'multiEvents'

class MyTest < Minitest::Test
  def test_pci_redaction
    result = pci_redaction()
    assert_equal "hello world!", result
  end
end
