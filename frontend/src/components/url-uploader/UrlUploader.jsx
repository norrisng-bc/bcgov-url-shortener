import './UrlUploader.css';
import { useState } from 'react'

const UrlUploader = () => {
  const [showLongUrl, setShowShorten] = useState(false)
  const [customString, setCustomString] = useState('')
  const [longUrl, setLongUrl] = useState('')
  const [shortUrl, setShortUrl] = useState('')

  const toggleState = () => {
    if (!longUrl) return;
    let displayUrl = 'https://short.gov.bc.ca/'

    if (customString) {
      displayUrl += customString
    } else {
      displayUrl += Array.from(Array(4), () => Math.floor(Math.random() * 36).toString(36)).join('')
    }
    setShortUrl(displayUrl)
    if (showLongUrl) {
      setLongUrl('')
      setCustomString('')
    }
    setShowShorten(!showLongUrl)
  }

  const handleKeyPress = (event) => {
    if(event.key === 'Enter'){
      toggleState()
    }
  }
  const handleFocus = (e) => e.target.select()


  if (showLongUrl) {
    return (
      <div className="url-container">
        <div className="url-label tl">Your Long URL</div>
        <input onFocus={handleFocus} readOnly className="text-input" value={longUrl} type='text'></input>
        <div className="url-label tl">Shortened URL</div>
        <input onFocus={handleFocus} readOnly className="text-input" value={shortUrl} type='text'></input>
        <button 
          className="BC-Gov-PrimaryButton-Dark" 
          type="button" 
          name="button"
          onClick={toggleState}
        >Shorten another</button>
      </div>
    );
  } else {
    return (
      <div className="url-container">
        <div className="url-label tl">Shorten a URL</div>
        <input
          autoFocus
          className="text-input" 
          value={longUrl} 
          onChange={e => setLongUrl(e.target.value)}
          onKeyDown={e => handleKeyPress(e)}
          type='text'>
        </input>
        <div className="url-label tl">Custom short link (Optional)</div>
        <input
          value={customString}
          className="text-input" 
          onChange={e => setCustomString(e.target.value)}
          onKeyDown={e => handleKeyPress(e)}
          type='text'>
        </input>
        <button 
          className="BC-Gov-PrimaryButton-Dark" 
          type="button" 
          name="button"
          onClick={toggleState}
        >Shorten</button>
      </div>
    );
  }

}

export default UrlUploader