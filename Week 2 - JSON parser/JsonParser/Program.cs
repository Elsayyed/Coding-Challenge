using System;

namespace JsonParser
{
    public enum TokenType
    
    { 
        LeftCurlyBrace,
        RightCurlyBrace,
        Colon,
        Comma,
        String,
        Number,
        True,
        False,
        Null,
        Invalid
    }

    /*
        The token will consist of the building blocks of the known
        block that exists in JSON files such as --> { } , " : []
    */
    public class Token(TokenType type, string? value = null)
    {
        public TokenType _type { get; } = type;
        public string _value { get; } = value;
    }

    public class Lexer
    {
        // public string? 
        private readonly string _inputString;
        private int _position;

        public Lexer(string inputString){
            _inputString = inputString;
            _position = 0;
        }

        public Token[] Tokenize() {
            
            var tokens = new List<Token>();

            while (_position < _inputString.Length){
                char currentChar = _inputString[_position++];

                switch (currentChar) 
                {
                    case '{':
                        tokens.Add(new Token(TokenType.LeftCurlyBrace));
                        break;
                    case '}':
                        tokens.Add(new Token(TokenType.RightCurlyBrace));
                        break;
                    case ':':
                        tokens.Add(new Token(TokenType.Colon));
                        break;
                    case ',':
                        tokens.Add(new Token(TokenType.Comma));
                        break;
                    case '"':
                        tokens.Add(new Token(TokenType.String, parseString(_inputString)));
                        break;
                    case '\n' or '\r':
                        break;
                    case ' ':
                        break;
                    default:
                        tokens.Add(new Token(TokenType.Invalid));
                        break;
                }
            }
            
             return tokens.ToArray();
        }

        private string? parseString(string _inputString)
        {
            string word = string.Empty;
            
            //Iterate over the string
            while(_position < _inputString.Length && _inputString[_position] != '"') {
                word += _inputString[_position++];
            }

            //To skip the last quotation closing the string.
            _position++;

            return word;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            //  Read from a file
            try
            {
                //Get the current project directory to direct the stream reader to the proper json file.
                string workingDirectory = Environment.CurrentDirectory;
                string projectDirectory = Directory.GetParent(workingDirectory).Parent.Parent.FullName;
                Console.WriteLine(projectDirectory);

                using (var sr = new StreamReader($"{projectDirectory}\\valid.json"))
                {
                    string fileContent = sr.ReadToEnd();

                    Lexer tester = new Lexer(fileContent);
                    Token[] test = tester.Tokenize();
                    
                    // Console.WriteLine($"Test 1: {test[1]._type}");
                    // Console.WriteLine(test);
                    // for (int _charPos = 0; _charPos < fileContent.Length; _charPos++)
                    // {
                    //     switch (fileContent[_charPos]) {}
                    // }
                    // Console.WriteLine(fileContent);

                }

            }
            catch (IOException e)
            {
                Console.WriteLine("Couldn't read the file");
                Console.WriteLine(e.Message);
            }
            
            //  Split lines based on new line
            //  Split lines based on spaces and create an array
        }
    }
}

